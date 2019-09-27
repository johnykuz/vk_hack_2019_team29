import json
import sqlite3
from collections import defaultdict

import numpy as np
from flask import jsonify


class SQL_Manager:

    def __init__(self):
        self.connection = sqlite3.connect('marketplace.db',
                                          check_same_thread=False)
        self.cursor = self.connection.cursor()


        products_create_query = '''CREATE TABLE IF NOT EXISTS products
                          (id INTEGER,
                           photo_url INTEGER,
                           description TEXT,
                           price INTEGER)'''


        users_create_query = '''CREATE TABLE IF NOT EXISTS users
                              (id INTEGER,
                               citizen_id INTEGER,
                               relative INTEGER)'''

        self.cursor.execute(products_create_query)
        self.cursor.execute(users_create_query)

    def category(self, category_id, user_id):
    	get_query = f'''SELECT * FROM products
    				    WHERE category={category_id} AND 
    				   		 _ROWID_ >= (abs(random()) % (SELECT max(_ROWID_) FROM bar))
    				   	LIMIT 20'''

    	data = self.cursor.execute(get_query).fetchall()

    	output = []
    	for product in data:
    		print(product)

    	response = jsonify(output)
    	response.status_code = 200
    	return response