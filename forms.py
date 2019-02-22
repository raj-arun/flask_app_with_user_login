from flask_wtf import FlaskForm
from  wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
    				validators = [DataRequired(), Length(min=4, max=25)])
    email = StringField('Email',
    				validators = [DataRequired(), Email()])
    password = PasswordField('New Password', validators = [DataRequired()])
    confirm = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email',
    				validators = [DataRequired(), Email()])
    password = PasswordField('New Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
