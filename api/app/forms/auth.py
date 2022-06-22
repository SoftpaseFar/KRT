from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError

from app.models.user import User


def validate_nickname(field):
  if User.query.filter_by(nickname=field.data).first():
    raise ValidationError("昵称已被注册")


def validate_email(field):
  if User.query.filter_by(email=field.data).first():
    raise ValidationError("电子邮件已被注册")


class RegisterForm(Form):
  email = StringField(
    label='email',
    validators=[
      DataRequired(message='邮箱不能为空'),
      Length(8, 64),
      Email(message='电子邮箱不符合规范'),
      validate_email
    ])
  password = PasswordField(
    label='password',
    validators=[
      DataRequired(message='密码不能为空，请输入密码'),
      Length(6, 32)
    ])

  nickname = StringField(
    label='nickname',
    validators=[
      DataRequired(message='昵称不能为空，请输入昵称'),
      Length(2, 10, message='昵称最少两个字符，最多10个字符'),
      validate_nickname
    ])


class LoginForm:
  email = StringField(
    label='email',
    validators=[
      DataRequired(message='邮箱不能为空'),
      Length(8, 64),
      Email(message='电子邮箱不符合规范'),
      validate_email
    ])
  password = PasswordField(
    label='password',
    validators=[
      DataRequired(message='密码不能为空，请输入密码'),
      Length(6, 32)
    ])



