# api蓝图
from flask import Blueprint

api = Blueprint('api', __name__)

from app.api import hello

