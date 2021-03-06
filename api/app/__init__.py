from flask import Flask
from . import secure
from . import setting
from app.models.base import db
from flask_login import LoginManager

# 用户登录模块定制
login_manager = LoginManager()


def create_app():
  app = Flask(__name__)

  app.config.from_object(secure)
  app.config.from_object(setting)
  print(app.config["DEBUG"])

  register_blueprint(app)

  login_manager.init_app(app)

  db.init_app(app)
  db.create_all(app=app)
  return app


def register_blueprint(app):
  from app.api import api
  app.register_blueprint(api)
  from app.web import web
  app.register_blueprint(web)
