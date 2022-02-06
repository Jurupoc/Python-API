from model import user
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import constant as const

_USER = user.User


class Database(object):
    """sqlite3 database class that holds testers jobs"""
    DB_LOCATION = const.DB_PATH

    def __init__(self):
        """Initialize db class variables"""
        self.engine = create_engine(Database.DB_LOCATION)
        self.connection = self.engine.connect()

    def get(self):
        with Session(self.engine) as session:
            query = session.query(_USER)
            return query

    def add(self, _user):
        with Session(self.engine) as session:
            session.add(_user)
            session.commit()

