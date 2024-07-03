from os import path
import os 

# Define database name
DB_NAME = "movies.db"

class Config:
    # SQLite database URI with fallback to sqlite:///movies.db if DATABASE_URL is not set
    SECRET_KEY = 'sanmiareoye'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OMDB_API_KEY = '3d7768ec'
