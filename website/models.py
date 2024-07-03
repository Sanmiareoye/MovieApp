from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  mylist =db.relationship('MyList')

class MyList(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   imdbId = db.Column(db.String(100), nullable=False)
   date = db.Column(db.DateTime(timezone=True), default=func.now())
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


