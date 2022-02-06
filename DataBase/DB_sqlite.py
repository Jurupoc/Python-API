from model import user
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import constant as const

_USER = user.User


class DBError(Exception):
    """ Base Class for all Database Error """
    pass


class EmailAlreadyAdd(DBError):
    """ Raises when the Email is already in the Database (at add() method) """
    pass


class DBConnectionError(DBError):
    """ Raises when is not possible to connect the database """
    pass


class Database(object):
    DB_LOCATION = const.DB_PATH

    def __init__(self):
        try:
            self.engine = create_engine(Database.DB_LOCATION)
            self.connection = self.engine.connect()

        except DBConnectionError:
            raise DBConnectionError("Error in the Database Connection")

    def get(self):
        with Session(self.engine) as session:
            query = session.query(_USER)
            return query

    def add(self, _user):
        with Session(self.engine) as session:
            session.add(_user)
            session.commit()



