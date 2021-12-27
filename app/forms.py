from flask_wtf import FlaskForm
from flask_wtf.html5 import EmailField, URLField
from wtforms import TextField, PasswordField, SubmitField, BooleanField
from wtforms.validators import EqualTo, InputRequired, Length



class SignUpForm(FlaskForm):
    email = EmailField('')
    username = TextField('', validators=[InputRequired('field is required'), Length(
        max=15, message='username cannot be more than 15 characters long')])
    password = PasswordField('', validators=[InputRequired('field is required'), Length(
        min=8, message='password must be at least 8 characters')])
    confirm_password = PasswordField('', validators=[InputRequired(
        'field is required'), EqualTo('password', message='password must match'), Length(min=8)])
    signup = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = EmailField('', validators=[InputRequired('field is required')])
    password = PasswordField('', validators=[InputRequired('field is required')] )
    remember_me = BooleanField('remember me?')
    login = SubmitField('Sign In')

    
class UrlAddForm(FlaskForm):
    name = TextField('', validators=[ InputRequired('field is required'), 
                    Length(max = 30,message='name cannot be more than 30 characters long')])
    url = URLField(validators=[InputRequired('field is required')])
    add_url = SubmitField('Add')
