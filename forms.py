from wtforms import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Length, InputRequired


class TestForm(Form):
    Field = StringField("Field", validators=[Length(4, 40), InputRequired()])
    submit = SubmitField("Submit")
