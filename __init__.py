from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flaskext.markdown import Markdown

# create Flask class object named myobj
myobj = Flask(__name__,static_url_path="", static_folder="static")
ckeditor =  CKEditor(myobj)
Markdown(myobj, extensions=['fenced_code'],auto_escape=True)
#PageDown(myobj)
# Flask login manager
login_manager = LoginManager()
login_manager.init_app(myobj)
login_manager.login_view = 'login'


myobj.config.from_mapping(
    SECRET_KEY = 'you-will-know',
    # location of sqlite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    
)

db = SQLAlchemy(myobj)
migrate = Migrate(myobj,db)

from myapp import routes, models
