from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
class ShareNoteForm(FlaskForm):
    '''
    Create form filed for the purpose of delete account information.
        Parameters:
            FlaskForm : A form parameter from flask_wtf
    '''
    email = StringField('Please enter the email of the person you want to share', validators=[DataRequired()])
    noteSharing = StringField('Please enter the note title you want to share', validators=[DataRequired()])
    share = SubmitField('Share')