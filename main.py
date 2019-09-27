from flask import Flask, json, request, jsonify
from sql_manager import SQL_Manager
from flask_cors import CORS, cross_origin



app = Flask(__name__)
sql_manager = SQL_Manager()


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def main():
    return 'OK'


@app.route('/category/<int:user_id>/<int:category_id>', methods=['GET'])
@cross_origin()
def category(user_id, category_id):
	return sql_manager.get_category(category_id, user_id)


@app.route('/profile/<int:user_id>', methods=['GET'])
@cross_origin()
def profile():
	return sql_manager.get_profile(user_id)


@app.route('/cart/<int:user_id>', methods=['GET'])
def cart():
	pass


@app.route('/product/<int:product_id>', methods=['GET'])
def product():
	pass


@app.route('/manage_cart/<int:user_id>/<int:product_id>/<int:method>', methods=['GET'])
def manage_cart():
	pass


@app.route('/manage_favourite/<int:user_id>/<int:product_id>/<int:method>', methods=['GET'])
def manage_favourite():
	pass


@app.route('/favourite/<int:user_id>', methods=['GET'])
def favourite(user_id):
	return sql_manager.get_faourites(user_id)



@app.route('/user/<int:user_id>/new_data', methods=['POST'])
def new_data():
	pass


@app.route('/search/<int:user_id>', methods=['POST'])
def search():
	pass



@app.route('/imports', methods=['POST'])
def import_data():
	print(request.data)
	data = json.loads(request.data)
	print(data)

	response = jsonify({'response':200})
	response.status_code = 200
	return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)