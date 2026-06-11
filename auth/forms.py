from wtforms import Form, StringField, PasswordField, EmailField, validators
class RegistrationForm(Form):
     username = StringField('Username', [
        validators.Length(min=4, max=25),
        validators.DataRequired()
    ])
