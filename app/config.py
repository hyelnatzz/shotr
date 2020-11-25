import os

class Config:
    SQLALCHEMY_DATABASE_URL = 'sqlite:///shorter.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(8).hex()
