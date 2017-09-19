from wtforms import Form, BooleanField, StringField, validators


class LoginForm(Form):
    name = StringField('name', [validators.DataRequired(), validators.Length(min=4, max=25)])
