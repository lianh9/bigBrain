from datetime import datetime
from flask_login.mixins import UserMixin
from sqlalchemy.orm import backref
from myapp import db
from myapp import login_manager
from markdown import markdown

class User(db.Model, UserMixin):
    '''
    Create user database for the purpose of storing user information.
        Parameters:
            db.Model :
            UserMixin: 
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash =db.Column(db.String(128))
    notes = db.relationship('Notes',backref='user',lazy = True)
 #Returns a string as a representation of the object.
    def __repr__(self):
        return f'<{self.id} {self.username}  {self.email}  {self.password_hash}>'
   
@login_manager.user_loader
def load_user(id):
    '''
    load user's id
        Parameters:
                id     
        Returns:
            int (id) : user id
    '''
    return User.query.get(int(id))

class Notes(db.Model):
    '''
    Create database to store notes information.
        Parameters:
            db.Model 
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    text = db.Column(db.Text)
    date_added = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)

 #Returns a string as a representation of the object.
    def __repr__(self):
        return f'<{self.title}  {self.text} >'
    

class Todo(db.Model):
    '''
    Creates a database to store the name and date
    for the todo list
        Parameters:
            db.Model
        Returns:
            String
    '''
    id = db.Column(db.Integer, primary_key = True)
    goal = db.Column(db.String(80))
    prio = db.Column(db.Integer, index = True)
    due_date = db.Column(db.DateTime)

    def __ref(self):
        return f"Todo('{self.goal}', {self.prio})"

class Tracker(db.Model):
    '''
    Creates a database to store the number and date
    to track how many hours they worked
        Parameters:
            db.model
        Returns:
            Date
            integer
    '''
    id = db.Column(db.Integer, primary_key = True)
    hours = db.Column(db.Integer)
    datew = db.Column(db.DateTime)

class FlashCard(db.Model):
    '''
    Create database to store flashcard information.
        Parameters:
            db.Model
        Returns:
            return html pages
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.String(128))
    date_added = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)

 #Returns a string as a representation of the object.
    def __repr__(self):
        return f'<{self.title}  {self.content} {self.date_added}  >'
