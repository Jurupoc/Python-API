from flask import Flask, request, jsonify
from flask_restful import Api
from model import user
from DataBase import DB_sqlite as Db

db_connect = Db.Database()

app = Flask(__name__)
api = Api(app)


@app.route('/users', methods=['GET'])
def get_users():
    result = []
    query = db_connect.get()
    for row in query:
        result.append(str(row))
    return jsonify(result)


@app.route('/users', methods=['POST'])
def add_users():
    result = []

    email = request.form.get('email')
    password = request.form.get('password')

    new_user = user.User(email, password)
    db_connect.add(new_user)

    query = db_connect.get()
    for row in query:
        result.append(str(row))

    return jsonify(result)


if __name__ == '__main__':
    app.run()
