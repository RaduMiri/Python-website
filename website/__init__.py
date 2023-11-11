# This makes the website folder a python package, essentailly we can import this folder

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path #we use it to find the folder we need 

#db is a database object and we can name it like bellow
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #__name__ is the name of the file that is ran, it's just to initialize flask
    app.config['SECRET_KEY'] = 'jsdfgdsflf' # for encoding, I just pressed random keys
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) #This just tells the database object to initialize the database with the app

    #now we put the routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from . import models #we put it just so we have the classes created so we can reference them here
    
    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/'+DB_NAME): #the name of the folder 
        #db.create_all(app=app) #we need to tell SQLAlchemy which app to use, we have only one and it is called app
        with app.app_context():
            db.create_all()
        print("Created Database!")
