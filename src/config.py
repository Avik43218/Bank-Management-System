import os

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
