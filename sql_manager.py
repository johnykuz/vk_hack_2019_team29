import json
import sqlite3
from collections import defaultdict

from flask import jsonify


class SQL_Manager:

    def __init__(self):
        self.connection = sqlite3.connect('marketplace.db',
                                          check_same_thread=False)
        self.cursor = self.connection.cursor()


        products_create_query = '''CREATE TABLE IF NOT EXISTS products
                          (id INTEGER,
                           photo_url INTEGER,
                           category INTEGER,
                           name TEXT,
                           description TEXT,
                           price INTEGER)'''


        users_create_query = '''CREATE TABLE IF NOT EXISTS users
                              (id INTEGER,
                               picture_url TEXT,
                               cash_back INT,
                               user_of_psb INT,
                               country TEXT,
                               city TEXT,
                               street TEXT,
                               building TEXT,
                               flat TEXT
                               )'''

        self.cursor.execute(products_create_query)
        self.cursor.execute(users_create_query)


    def get_category(self, category_id, user_id):
    	get_query = f'''SELECT * FROM products
    				    WHERE category={category_id} AND 
    				   		 _ROWID_ >= (abs(random()) % (SELECT max(_ROWID_) FROM products))
    				   	LIMIT 20'''

    	data = self.cursor.execute(get_query).fetchall()

    	output = []
    	for product in data:
    		temp = {'id': product[0], 'photo_url': product[1], 'name': product[3],
    			    'description': product[4], 'price': product[5]}
    		output.append(temp)

    	response = jsonify({'items': output})
    	response.status_code = 200
    	return response


    def get_profile(self, user_id):
    	get_query = f'''SELECT * FROM users
    				   WHERE id = {user_id}'''
    	data = self.cursor.execute(get_query).fetchone()

    	fields = ['picture_url', 'cash_back', 'user_of_psb', 'country', 'city', 'street', 'building', 'flat']
    	output = {}
    	for i in range(len(data)):
    		output[field] = data[i+1]

    	response = jsonify({'user': output})
    	response.status_code = 200
    	return response
