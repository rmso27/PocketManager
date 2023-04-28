from flask import Flask
from .db_funcs import db_init

app = Flask(__name__)
db_init()

from app import routes