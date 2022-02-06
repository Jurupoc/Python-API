from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import constant as const

Base = declarative_base()
engine = create_engine(const.DB_PATH)


def create_table():
    Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f'User: {self.email}'

    def __str__(self):
        return f'Email: {self.email}'


