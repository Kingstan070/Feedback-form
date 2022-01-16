from flask import Flask
from .config import DB_config
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# Starting a flask object
app = Flask(__name__)

#setting all config keys
app.config['SECRET_KEY'] = 'Hard_guess_string_but_not_that_hard'

#   data base details
dbd = DB_config(host="localhost",
                user="root",
                password="toor",
                port="3306",
                database='CURD')
                            

# Import routing to render the pages
from . import views
from .models import create_db

# To create database if it dosen't exist
create_db()