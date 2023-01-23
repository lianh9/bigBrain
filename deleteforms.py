from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
class DeleteForm(FlaskForm):
    '''
    Create form filed for the purpose of delete account information.
        Parameters:
            FlaskForm : A form parameter from flask_wtf
    '''
    email = StringField('Email', validators=[DataRequired()])
    password_hash = PasswordField('Password',validators=[DataRequired()])
    delete = SubmitField('Submit')