from wtforms import StringField, Form
from wtforms.validators import DataRequired


class TextClassifyForm(Form):
  content = StringField(
    label='content',
    validators=[
      DataRequired()
    ])
  title = StringField(
    label='title',
    validators=[
      DataRequired()
    ])
