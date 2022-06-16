from wtforms import FloatField, Form
from wtforms.validators import DataRequired


class WeatherForm(Form):
  latitude = FloatField(
    label='latitude',
    validators=[
      DataRequired()
    ])

  longitude = FloatField(
    label='longitude',
    validators=[
      DataRequired()
    ])
