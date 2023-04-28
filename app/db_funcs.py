## IMPORTS ##

# Import modules
from .database import Database

## FUNCTIONS ##

# Initialize database
def db_init():
    Database.initialize()

# Create user
def insert_user():

    Database.insert_one('users', {
            "name": "Ruben",
            "username": "rmso27",
            "password": "Password"
        })
