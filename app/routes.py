## IMPORTS ##

# Import modules
from flask import request, render_template
from app import app
import configparser

# Import functions
from .db_funcs import db_init, insert_user


## MAIN VARS ##

# Setup configuration file
config = configparser.ConfigParser()
config.read('configs/configs.ini')

# Read configuration file


## ROUTES ##

# Home
@app.route('/')
def home():

    return render_template("public/index.html")

# Login
@app.route('/login')
def login():

    return "Success"

# Register
@app.route('/register')
def register():

    return render_template("public/register.html")

# Register
@app.route('/create-account', methods =  ["POST"])
def create_account():

    insert_user()

    return "Success"