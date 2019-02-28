from opex.models import User
from flask_wtf import FlaskForm
from  wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
    				validators = [DataRequired(), Length(min=4, max=25)])
    email = StringField('Email',
    				validators = [DataRequired(), Email()])
    password = PasswordField('New Password', validators = [DataRequired()])
    confirm = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is already taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email is already used. Please choose a different one.')            

class LoginForm(FlaskForm):
    email = StringField('Email',
    				validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
