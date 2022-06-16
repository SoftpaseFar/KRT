from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
  x = StringField(validators=[DataRequired(), Length(min=1, max=30)])
  y = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)




