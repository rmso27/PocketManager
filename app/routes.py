## IMPORTS ##

# Import modules
from flask import request, render_template
from app import app
import configparser

# Import functions from 'functions' file


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