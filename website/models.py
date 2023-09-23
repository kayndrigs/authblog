#. means __init__
from . import db
from flask_login import UserMixin
from sql_alchemy.sql import func

# model = table 
# define all the columns that are going to be in our user table
class User(db.Model, UserMixin):
    # PK -> primary key generation
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.Date(timezone=True), default=funct.now())