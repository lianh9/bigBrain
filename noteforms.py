from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    '''
    Create form filed string and textarea for the purpose of entering notes and the title.
        Parameters:
            FlaskForm : A form parameter from flask_wtf
    '''
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()],widget=TextArea())
    submit = SubmitField('submit')
