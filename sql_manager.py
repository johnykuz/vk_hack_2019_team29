import json
import io
import sqlite3
import numpy as np
from collections import defaultdict

from flask import jsonify


class SQL_Manager:

    def __init__(self):
        self.connection = sqlite3.connect('marketplace.db',
                                          check_same_thread=False)
        self.cursor = self.connection.cursor()


        sqlite3.register_adapter(np.ndarray, self.adapt_array)
        sqlite3.register_converter("array", self.convert_array)

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
                               favourite array
                               )'''

        self.cursor.execute(products_create_query)
        self.cursor.execute(users_create_query)

        # self.connection.enable_load_extension(True)
        # self.connection.load_extension("./libsqliteicu.so")

    def adapt_array(self, arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(self, text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)

    def get_category(self, user_id, category_id):
        if category_id == 999:
            category_id = 0
            # category_id = classify user

        get_query = f'''SELECT * FROM products
                        WHERE category={category_id}
                        ORDER BY RANDOM()
                        LIMIT 20'''

        data = self.cursor.execute(get_query).fetchall()

        if data:
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
        response = jsonify({'error':'error'})
        response.status_code = 400
        return response

    def get_profile(self, user_id):
        get_query = f'''SELECT * FROM users
                       WHERE id = {user_id}'''
        data = self.cursor.execute(get_query).fetchone()

        fields = ['picture_url', 'cash_back', 'user_of_psb']
        output = {}
        if data:
            for i in range(len(fields)):
                output[fields[i]] = data[i+1]

        response = jsonify({'user': output})
        response.status_code = 200
        return response

    def get_product(self, product_id):
        get_query = f'''SELECT * FROM products
                       WHERE id={product_id}'''
        data = self.cursor.execute(get_query).fetchone()
        fields = ['id', 'photo_url', 'name', 'description', 'price']
        output = {}
        if data:
            for i in range(len(fields)):
                output[fields[i]] = data[i]
        return output

    def get_user_favourite(self, user_id):
        get_query = f'''SELECT favourite FROM users
                       WHERE id = {user_id}'''
        data = self.cursor.execute(get_query).fetchone()

        if data:
            output = []
            data = self.convert_array(data[0])

            for product in data:
                output.append(self.get_product(int(product)))
            response = jsonify({'items': output})
            response.status_code = 200

            return response
        response = jsonify({'items': []})
        response.status_code = 200
        return response

    def manage_favourite(self, user_id, product_id, method):
        get_query = f'''SELECT favourite FROM users
                        WHERE id = {user_id}'''
        data = self.cursor.execute(get_query).fetchone()

        if data:
            data = list(self.convert_array(data[0]))
            if method == 0:
                if product_id in data:
                    data.remove(product_id)
            else:
                if product_id not in data:
                    data.append(product_id)
            data = np.array(data)


            insert_query = f'''UPDATE users SET favourite=? WHERE id=?'''

            self.cursor.executemany(insert_query, [[data, user_id]])
            self.connection.commit()

    def search(self, string):
        string = string.lower()

        get_query = f"""SELECT * FROM products
                WHERE LOWER(name) LIKE {"'%" + string + "%'"}
                ORDER BY RANDOM()
                LIMIT 20"""
        data = self.cursor.execute(get_query)

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
        return respons