from wtforms import StringField, Form
from wtforms.validators import DataRequired


class EmotionAnalysisForm(Form):
  string = StringField(
    label='content',
    validators=[
      DataRequired()
    ])
