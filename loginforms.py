from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class LoginForm(FlaskForm):
    '''
    Create form filed for the purpose of login account information.
        Parameters:
            FlaskForm : A form parameter from flask_wtf
    '''
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password_hash = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


   


