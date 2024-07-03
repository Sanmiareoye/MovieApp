from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config, DB_NAME
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    from . import models

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app

def create_database(app):
  if not path.exists('website/' + DB_NAME):
    with app.app_context():
      db.create_all()
    print('Created Database!')