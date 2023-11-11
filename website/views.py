from flask import Blueprint, render_template #Blueprint just means it has a bunch of urls defined in it
from flask_login import login_required, current_user

views = Blueprint('views', __name__) #you don't have to name them views

@views.route('/') #Btw, this with @ is called a decorator
@login_required
def home(): #Because we set up a route, this function will run whenver we call / in the browser for this adress
    return render_template("home.html", user=current_user)