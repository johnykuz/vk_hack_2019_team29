from flask import Flask, json, request, jsonify
from sql_manager import SQL_Manager
from flask_cors import CORS, cross_origin
from model import Model


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


@app.route('/product/<int:user_id>/<int:product_id>', methods=['GET'])
@cross_origin()
def product(user_id, product_id):
    response = jsonify({'product': sql_manager.get_product(user_id, product_id)})
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
@cross_origin()
def user_login():
    data = json.loads(request.data)
    user_id = data['id']
    print(data)

    return sql_manager.get_category(user_id, 999)


@app.route('/sites', methods=['GET'])
@cross_origin()
def sites():
    links = ['https://loverepublic.ru/', 'https://www.wildberries.ru/', 'https://www.petshop78.ru/',
    'https://www.sportmaster.ru/', 'https://www.labirint.ru/',
     'https://www.citilink.ru/', 'https://www.citilink.ru/']

    pic_links = ['https://i.ibb.co/p3bKDzw/clothes.png', 'https://i.ibb.co/p3bKDzw/clothes.png',
     'https://i.ibb.co/YtwpvpH/sport.png', 'https://i.ibb.co/GHxHJb2/pets.png',
      'https://i.ibb.co/DQLwTBt/book.png', 'https://i.ibb.co/f19ZSmP/techology.png',
      'https://i.ibb.co/ZHtbvz3/game.png']

    names = ['LoveRepublic', 'WildBerries', 'PetShop78', 'Sportmaster', 'Labirint', 'Citilink', 'Citilink']

    output = []
    for i in range(len(links)):
        temp = {'photo_url': pic_links[i], 'link': links[i], 'name': names[i]}
        output.append(temp)

    response = {'sites': output}
    response.status_code = 201
    return response

if __name__ == '__main__':
    app.run()