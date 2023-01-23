from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class FlashCardForm(FlaskForm):
    '''
    Create form filed 2 string fields for the purpose of creating flashcards.
        Parameters:
            FlaskForm : A form parameter from flask_wtf
    '''
    title = StringField('Question', validators=[DataRequired()])
    content = StringField('Answer', validators=[DataRequired()])
    submit = SubmitField('Submit Flash Card')
