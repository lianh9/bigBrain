from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
class SearchForm(FlaskForm):
    '''
    Create form filed for the purpose of search word in the page.
        Parameters:
            FlaskForm : A form parameter from flask_wtf
    '''
    search = StringField('Please enter the word to search notes', validators=[DataRequired()])
    submit = SubmitField('Search')