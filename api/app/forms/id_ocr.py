from wtforms import StringField, Form
from wtforms.validators import DataRequired


class IdInfoForm(Form):
  front = StringField(
    label='front',
    validators=[
      DataRequired()
    ])

  negative = StringField(
    label='negative',
    validators=[
      DataRequired()
    ])
