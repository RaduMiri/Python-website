from flask import Blueprint, render_template, request, flash, redirect, url_for
#Render_template is to make a template object to be able to send a html page
#Flash is for flashing a message, request is for using getters on the html forms, and other requests
from .models import User #This is so I can create users
from werkzeug.security import generate_password_hash, check_password_hash #I do this to store passwords securely
from . import db #This gets it from __init__.py
from flask_login import login_user, login_required, logout_user, current_user #User stuff made easy with flask, TODO: maybe I should learn or do this user stuff myself?

#Btw, a hash function is just a function that doesn't have an inverse, which is why it's used for encrypting


auth = Blueprint('auth', __name__)

#In Jinja templating you can pass values right to the templates and use them in the html
#Routes should know what kind of request you are making POST, GET, etc...

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #data = request.form #This tells what kind of request from html you are making, or I think it might just get the form :))))
    if request.method == 'POST': #If we send a post method with data though login, get the sent data
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() #Filter query in the db by email, .first to only get the first, but it should be only 1 with this email anyway, it is unique
        if user:
            if check_password_hash(user.password, password): #It will check the hashed password we have stored against the password intorduced that is hashed in the same way
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) #The user will be remember anytime they access the website, unless the server is goes down or the user clears cache or stuff
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template('login.html', user=current_user) #write variable name here

@auth.route('/logout')
@login_required #This decorator makes it so a user must be logged in to be able to get logged out, because otherwise it doesn't make sense
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method=='POST':
        email = request.form.get('email') #Form getter
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #:TODO Stop reload if data is wrong, make sure it doesn't bug if I spam it, makes form easier to do
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters', category='error') #I can name the category whatever I want
        elif len(first_name)<2:
            flash('First name must be greater than 1 character', category='error')
        elif password1!=password2:
            flash("Passwords don't match", category='error')
        elif len(password1)<7:
            flash('Password must be greater than 6 character', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256')) #The method here is just a hashing algorithm, also sha256 didn't work, this seems to be the default method, maybe it works without specifying one
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created", category="success")
            return redirect(url_for('views.home')) #I could redirect to /home, but if i change the url for home this will break, it is safer to use the home function from views
    return render_template('sign_up.html', user=current_user)