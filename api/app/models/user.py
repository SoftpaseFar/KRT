from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float


class User(Base):
  # __tablename__ = 'user1'
  id = Column(Integer, primary_key=True)
  nickname = Column(String(24), nullable=False)
  phone_number = Column(String(18), unique=True)
  _password = Column("password", String(128), nullable=False)
  email = Column(String(50), unique=True, nullable=False)
  confirmed = Column(Boolean, default=False)
  beans = Column(Float, default=0)
  send_counter = Column(Integer, default=0)
  receive_counter = Column(Integer, default=0)
  wx_open_id = Column(String(50))
  wx_name = Column(String(32))

  # 属性的getter方法
  @property
  def password(self):
    return self._password

  # 属性的setter方法
  @password.setter
  def password(self, raw):
    self._password = generate_password_hash(raw)

  def check_password(self, raw):
    return check_password_hash(self._password, raw)

  # def get_user_form_id(self,id):
  #   self.
