import sqlite3


connection = sqlite3.connect('marketplace.db', check_same_thread=False)
cursor = connection.cursor()


products_create_query = '''CREATE TABLE IF NOT EXISTS products
                  (id INTEGER,
                   photo_url INTEGER,
                   category INTEGER,
                   description TEXT,
                   price INTEGER)'''


users_create_query = '''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER,
                       citizen_id INTEGER,
                       relative INTEGER)'''

cursor.execute(products_create_query)
cursor.execute(users_create_query)


link = 'https://c.dns-shop.ru/thumb/st1/fit_width/120/120/b31b95e5e3e5bea851387ee4b03f4618/acaac7f3e882bd9ef05986ffa238428d9b0eaeb45879fe557178c60f14be23cf.jpg.webp'
desc = '[RedVerg RD5461C-120A, RedVerg RD5461C-130A, RedVerg RD5461C-150A, RedVerg RD5461C-160B, пластик, 1 шт]'
query = '''INSERT INTO products VALUES (?, ?, ?, ?, ?)'''
params = []

for i in range(100):
  params.append([i, link, 0, desc, 160+i*10])

cursor.executemany(query, params)
connection.commit()