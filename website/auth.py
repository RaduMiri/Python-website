from flask import Blueprint, render_template, request, flash #Flash is for flashing a message

auth = Blueprint('auth', __name__)

#In Jinja templating you can pass values right to the templates and use them in the html
#Routes should know what kind of request you are making POST, GET, etc...
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form #This tells what kind of request from html you are making
    print(data)
    return render_template('login.html', boolean=True) #write variable name here

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method=='POST':
        email = request.form.get('email') #Form getter
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)<4:
            flash('Email must be greater than 3 characters', category='error') #I can name the category whatever I want
        elif len(firstName)<2:
            flash('First name must be greater than 1 character', category='error')
        elif password1!=password2:
            flash("Passwords don't match", category='error')
        elif len(password1)<7:
            flash('Password must be greater than 6 character', category='error')
        else:
            flash("Account created", category="success")
            #add user to database
    return render_template('sign_up.html')