from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField, StringField
from wtforms.validators import EqualTo, InputRequired, Length



class SignUpForm(FlaskForm):
    email = StringField('')
    username = StringField('', validators=[InputRequired('field is required'), Length(
        max=15, message='username cannot be more than 15 characters long')])
    password = PasswordField('', validators=[InputRequired('field is required'), Length(
        min=8, message='password must be at least 8 characters')])
    confirm_password = PasswordField('', validators=[InputRequired(
        'field is required'), EqualTo('password', message='password must match'), Length(min=8)])
    signup = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField('', validators=[InputRequired('field is required')])
    password = PasswordField('', validators=[InputRequired('field is required')] )
    remember_me = BooleanField('remember me?')
    login = SubmitField('Sign In')

    
class UrlAddForm(FlaskForm):
    name = StringField('', validators=[ InputRequired('field is required'), 
                    Length(max = 30,message='name cannot be more than 30 characters long')])
    url = StringField(validators=[InputRequired('field is required')])
    add_url = SubmitField('Add')
