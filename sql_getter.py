import sqlite3


connection = sqlite3.connect('marketplace.db', check_same_thread=False)
cursor = connection.cursor()


get_query = f'''SELECT * FROM products
			    WHERE category=0 AND
			   		 _ROWID_ >= (abs(random()) % (SELECT max(_ROWID_) FROM products))
			   	LIMIT 20'''

data = cursor.execute(get_query).fetchall()
print(data)

output = []
for product in data:
	print(product)

# response = jsonify(output)
# response.status_code = 200
# return response