from flask import Flask, json, request, jsonify
from sql_manager import SQL_Manager
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)
sql_manager = SQL_Manager()


@app.route('/')
@cross_origin()
def main():
    return 'OK'


@app.route('/category/<int:user_id>/<int:category_id>', methods=['GET'])
@cross_origin()
def category(user_id, category_id):
    return sql_manager.get_category(user_id, category_id)


@app.route('/profile/<int:user_id>', methods=['GET'])
@cross_origin()
def profile(user_id):
    return sql_manager.get_profile(user_id)


@app.route('/product/<int:product_id>', methods=['GET'])
@cross_origin()
def product(product_id):
    response = jsonify({'product': sql_manager.get_product(product_id)})
    response.status_code = 200
    return response

@app.route('/manage_favourite/<int:user_id>/<int:product_id>/<int:method>', methods=['GET'])
@cross_origin()
def manage_favourite(user_id, product_id, method):
    sql_manager.manage_favourite(user_id, product_id, method)
    return sql_manager.get_user_favourite(user_id)


@app.route('/favourite/<int:user_id>', methods=['GET'])
@cross_origin()
def favourite(user_id):
    return sql_manager.get_user_favourite(user_id)


@app.route('/search/<int:user_id>', methods=['POST'])
@cross_origin()
def search(user_id):
    data = json.loads(request.data)
    query = data['data']

    return sql_manager.search(query)

@app.route('/user/data', methods=['POST'])
def user_login():
    data = json.loads(request.data)
    user_id = data['id']

    return sql_manager.get_category(user_id, 999)


if __name__ == '__main__':
    app.debug = True
    app.run()