from wtforms import StringField, Form
from wtforms.validators import DataRequired


class SMSVerForm(Form):
  mobile = StringField(
    label='mobile',
    validators=[
      DataRequired()
    ])

  code = StringField(
    label='code',
    validators=[
      DataRequired()
    ])

