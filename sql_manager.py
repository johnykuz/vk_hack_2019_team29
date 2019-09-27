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
                           name TEXT,
                           description TEXT,
                           price INTEGER,
                           category INTEGER)'''


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

        fields = ['id', 'photo_url', 'name', 'description', 'price']
        output = []
        if data:
            for product in data:
                temp = {}

                for i in range(len(fields)):
                    temp[fields[i]] = product[i]

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
        if data:
            print(data)
            for i in range(len(fields)):
                output[fields[i]] = data[i+1]

        response = jsonify({'user': output})
        response.status_code = 200
        return response


    def get_product(self, product_id):
        get_query = f'''SELECT * FROM products
                       WHERE id={product_id}'''
        data = self.cursor.execute(get_query).fetchone()

        fields = ['id', 'photo_url', 'category', 'name', 'description', 'price']
        output = {}
        if data:
            for i in range(len(fields)):
                output[fields[i]] = data[i]

        response = jsonify({'product': output})
        response.status_code = 200

        return response
