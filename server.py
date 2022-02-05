from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine


db_connect = create_engine(r'sqlite:///.\sqlite\db\pythonsqlite.db')

app = Flask(__name__)

api = Api(app)


class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from user")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        email = request.form.get('email')
        password = request.form.get('password')
        conn.execute(
            "insert into user values(null, '{0}', '{1}')".format(email, password))

        query = conn.execute('select * from user order by id desc limit 1')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    # def put(self):
    #     conn = db_connect.connect()
    #     id = request.form.get['id']
    #     name = request.form.get['name']
    #
    #     conn.execute("update user set name ='" + str(name) + "'  where id =%d " % int(id))
    #
    #     query = conn.execute("select * from user where id=%d " % int(id))
    #     result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
    #     return jsonify(result)

    # def delete(self):
    #     conn = db_connect.connect()
    #     _id = request.form.get('id')
    #     conn.execute("delete from user where id=%d " % int(_id))
    #     return {"status": "success"}


api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run()
