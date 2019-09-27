import sqlite3
import io
import numpy as np


connection = sqlite3.connect('marketplace.db', check_same_thread=False)
cursor = connection.cursor()



def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())



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
                         flat TEXT,
                         cart BLOB
                         )'''

cursor.execute(products_create_query)
cursor.execute(users_create_query)


link = 'https://c.dns-shop.ru/thumb/st1/fit_width/120/120/b31b95e5e3e5bea851387ee4b03f4618/acaac7f3e882bd9ef05986ffa238428d9b0eaeb45879fe557178c60f14be23cf.jpg.webp'
name = '[RedVerg RD5461C-120A, RedVerg RD5461C-130A, RedVerg RD5461C-150A, RedVerg RD5461C-160B, пластик, 1 шт]'
query = '''INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)'''
params = []

for i in range(100):
  params.append([i, link, name, 'description_string', 160+i*10, 0])

cursor.executemany(query, params)
connection.commit()

cart = [1, 11, 21, 45, 12, 90, 32, 89]
insert_user = '''INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?, ?)'''
params = [0, 'https://images-na.ssl-images-amazon.com/images/I/8166xCVDGnL._SY355_.jpg', 100, 0, 'Russia', 'Perm', 'Bolshevikov', '89', '1', adapt_array(cart)]

cursor.executemany(insert_user, [params])
connection.commit()