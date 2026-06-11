from wtforms import Form, StringField, PasswordField, EmailField, validators
class RegistrationForm(Form):
     username = StringField('Username', [
        validators.Length(min=4, max=25),
        validators.DataRequired()
    ])
     email = EmailField('Email Address', [
        validators.Length(min=6, max=35),
        validators.Email(),
        validators.DataRequired()
    ])
