from flask import Flask, request, jsonify
from flask_restful import Api
from sqlalchemy import create_engine


db_connect = create_engine(r'sqlite:///.\sqlite\db\pythonsqlite.db')

app = Flask(__name__)
api = Api(app)


@app.route('/users', methods=['GET'])
def get_users():
    conn = db_connect.connect()
    query = conn.execute("select * from user")
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return jsonify(result)


@app.route('/users', methods=['POST'])
def add_users():
    conn = db_connect.connect()

    email = request.form.get('email')
    password = request.form.get('password')

    conn.execute(
        "insert into user values(null, '{0}', '{1}')".format(email, password))

    query = conn.execute('select * from user order by id desc limit 1')
    result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    return jsonify(result)


if __name__ == '__main__':
    app.run()
