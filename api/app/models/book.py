from sqlalchemy import Column, Integer, String
from app.models.base import db


class Book(db.Model):
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)
  author = Column(String(30), default='未名')
  isbn = Column(String(15), nullable=False, unique=True)
  test = Column(String(30), default='测试')

  def sample(self):
    pass
