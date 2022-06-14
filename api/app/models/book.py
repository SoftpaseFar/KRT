from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)
  author = Column(String(30), default='未名')
  isbn = Column(String(15), nullable=False, unique=True)

  def sample(self):
    pass
