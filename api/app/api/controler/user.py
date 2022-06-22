from flask import jsonify, request
from app.models.base import db
from app.api import api
from app.forms.auth import RegisterForm, LoginForm
from app.models.user import User


# 用户注册
@api.route("/v1/user/register", methods=['POST'])
def register():
  form = RegisterForm(request.form)
  if form.validate():
    user = User()
    user.set_attrs(form.data)
    db.session.add(user)
    db.session.commit()
  return jsonify(
    form.errors
  )


# 用户登录
@api.route("/v1/user/login", methods=['POST'])
def login():
  form = LoginForm(request.form)
  user = User.query.filter_by(email=form.email.data).first()
  if user and user.check_password(form.password.data):
    pass
  else:
    return jsonify({
      'status': '211',
      'msg': "账号不存在或密码错误"
    })

# 修改密码
# 待开发
