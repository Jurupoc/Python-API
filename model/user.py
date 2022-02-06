from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import constant as const
from cryptography import encoder

Base = declarative_base()
engine = create_engine(const.DB_PATH)


def create_table():
    Base.metadata.create_all(engine)


def _encoder_password(self, password):
    return encoder(password)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = self._encoder_password(password)

    def __repr__(self):
        return f'Email: {self.email}'

    def __str__(self):
        return f'Email: {self.email}'



