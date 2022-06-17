from wtforms import StringField, Form
from wtforms.validators import DataRequired

class StuVerForm(Form):
  verif_code = StringField(
    label='verif_code',
    validators=[
      DataRequired()
    ])
