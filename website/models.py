# For database models

from . import db
from flask_login import UserMixin #Custom class that gives users for flask login
from sqlalchemy.sql import func #we use it for the default datetime

#Whenever we want to make a database model we name it and make it inheirt form db.Model

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func.now() just gets the current date and time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Even though we wrote the class User, in the database it will be written user, btw, this is one-to-many

class User(db.Model, UserMixin): #We make it inherit both because we will use it to store Users
    #Now we make the columns
    id = db.Column(db.Integer, primary_key=True) #whatever we would write in SQL
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #We have to do it both ways, even though it will not make a new column, also we need to be the exact name of the class in python

