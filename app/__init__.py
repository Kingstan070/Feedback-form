from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import os

# basedir = os.path.abspath(os.path.dirname(__file__))

# Starting a flask object
app = Flask(__name__)

#setting all config keys
app.config['SECRET_KEY'] = 'hardtoguess'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
# db = SQLAlchemy(app)

# Import routing to render the pages
from . import views