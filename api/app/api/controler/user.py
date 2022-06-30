from flask import jsonify, request
from app.api.service.user_token import user_token_get
from app.models.base import db
from app.api import api
from app.forms.auth import RegisterForm, LoginForm, TokenForm
from app.models.user import User


# from flask_login import login_user


# 用户注册
@api.route("/v1/user/register", methods=['POST'])
def register():
  form = RegisterForm(request.form)
  if form.validate():
    user = User()
    user.set_attrs(form.data)
    db.session.add(user)
    db.session.commit()
    return jsonify({
      'status': '200',
      'msg': "注册成功"
    })
  else:
    return jsonify({
      'status': '211',
      'msg': form.errors
    })


# 用户登录
@api.route("/v1/user/login", methods=['POST'])
def login():
  form = LoginForm(request.form)
  user = User.query.filter_by(email=form.email.data).first()
  if user and user.check_password(form.password.data):
    return jsonify({
      'status': '200',
      'token': user.id,
      'msg': '登陆成功'
    })
  else:
    return jsonify({
      'status': '211',
      'msg': "账号不存在或密码错误"
    })


# 修改密码

# 待开发

# 获取Token
@api.route("/v1/user/token", methods=['POST'])
def token():
  form = TokenForm(request.args)
  if form.validate():
    res = user_token_get(form.code.data)
    return jsonify(res)
  else:
    return jsonify({
      'status': '211',
      'msg': "账号不存在或密码错误"
    })
