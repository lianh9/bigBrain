
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class Track(FlaskForm):
    '''
        Create form filed for the purpose of tracking hours worked.
                Parameters:
                FlaskForm : A form parameter from flask_wtf
    '''
    hours = IntegerField("How many hours did you work")
    datew = DateField("When did you work(m/d/y)",format = '%m/%d/%Y')
    addH = SubmitField("Save Hours")
