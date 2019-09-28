import sqlite3
import io
import numpy as np
import pandas as pd


connection = sqlite3.connect('marketplace.db', check_same_thread=False)
cursor = connection.cursor()

def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)


sqlite3.register_adapter(np.ndarray, adapt_array)
sqlite3.register_converter("array", convert_array)

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

cursor.execute(products_create_query)
cursor.execute(users_create_query)


link = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT2XPE7EHN5jHcPueDwZBG0vTIhSDcOoyxCPP7z_7qY-0CeWBg1  '
name = '[RedVerg RD5461C-120A, RedVerg RD5461C-130A, RedVerg RD5461C-150A, RedVerg RD5461C-160B, пластик, 1 шт]'
query = '''INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)'''

idx = 0
params = []
data = pd.read_csv('products_final.csv')
for row in data.iterrows():
  idx += 1
  params.append([idx, row[1][3],  row[1][1], row[1][2], row[1][4], row[1][5]])
print(idx)
cursor.executemany(query, params)
connection.commit()

cart = np.array([1, 11, 21, 45, 12, 90, 32, 89])
insert_user = '''INSERT INTO users VALUES (?,?,?,?,?)'''
params = [0, 'https://images-na.ssl-images-amazon.com/images/I/8166xCVDGnL._SY355_.jpg', 100, 0, cart]

cursor.executemany(insert_user, [params])
connection.commit()