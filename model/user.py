from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from cryptography import encoder
import constant as const

Base = declarative_base()
engine = create_engine(const.DB_PATH_2)


def create_table():
    Base.metadata.create_all(engine)


def _encoder_password(password):
    return encoder(password)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = _encoder_password(password)

    def __repr__(self):
        return f'Email: {self.email}'

    def __str__(self):
        return f'Email: {self.email}'
