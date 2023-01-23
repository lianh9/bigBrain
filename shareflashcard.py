from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ShareCardForm(FlaskForm):
    """
    Create form filed 2 string fields for the purpose of creating flashcards.
        Parameters:
            FlaskForm : A form parameter from flask_wtf
    """
    share_user_name = StringField('Share With', validators=[DataRequired()])
    card_id = StringField('Card ID', validators=[DataRequired()])
    submit = SubmitField('Submit Flash Card')
