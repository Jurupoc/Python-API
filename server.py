from flask import Flask, request, jsonify
from flask_restful import Api

from model import user
from DataBase import DB_sqlite as Db

db_connect = Db.Database()

app = Flask(__name__)
api = Api(app)


class APIError(Exception):
    """ All possible Exceptions """
    pass


class UserDataError(APIError):
    """ Raises when nether the Email or Password are None"""
    code = 403
    description = "User Data Error"


@app.errorhandler(APIError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {"error": err.description, "message": ""}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    # Add some logging so that we can monitor different types of errors
    app.logger.error(f"{err.description}: {response['message']}")
    return jsonify(response), err.code


@app.errorhandler(500)
def handle_exception(err):
    """Return JSON instead of HTML for any other server error"""
    app.logger.error(f"Unknown Exception: {str(err)}")
    response = {"error": "Sorry, that error is on us, please contact support if this wasn't an accident"}
    return jsonify(response), 500


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

    if not email or not password:
        raise UserDataError('Email or Password can not be None')

    new_user = user.User(email, password)
    db_connect.add(new_user)

    query = db_connect.get()
    for row in query:
        result.append(str(row))

    return jsonify(result)


if __name__ == '__main__':
    app.run()
