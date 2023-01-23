from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class ToDo(FlaskForm):
    '''
            Create form filed for the purpose of creating a to do list.
                    Parameters:
                    FlaskForm : A form parameter from flask_wtf
    '''
    goal = StringField(  "What to do            :", validators = [DataRequired()])
    prio = IntegerField("Priority rank:", validators = [DataRequired()])
    due_date = DateField("When is it due?(m/d/y):", validators = [DataRequired()], format = '%m/%d/%Y')
    addG = SubmitField("Add to do")
    delG = SubmitField("Remove item")
