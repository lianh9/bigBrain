from markdown import markdown
import pdfkit
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

'''
get the file
'''


class GetFile(FlaskForm):
    file = FileField()
