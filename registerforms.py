from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

 
class RegisterForm(FlaskForm):
    '''
    Create form filed for the purpose of signing up account information.
        Parameters:
            FlaskForm : A form parameter from flask_wtf
    '''
    username = StringField('Username', validators=[DataRequired()])
    password_hash = PasswordField('Password',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    register = SubmitField('Sign up')

