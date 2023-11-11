from flask import Blueprint, render_template, request, flash, jsonify #Blueprint just means it has a bunch of urls defined in it
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) #you don't have to name them views

@views.route('/', methods=['GET', 'POST']) #Btw, this with @ is called a decorator
@login_required
def home(): #Because we set up a route, this function will run whenver we call / in the browser for this adress
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note)<1:
            flash('NOte is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST']) #Why not just use a delete request, that return is strange
def delete_note():
    data = json.loads(request.data) #Takes data from a post request as a json object or python dictionary
    noteId = data['noteId']
    note = Note.query.get(noteId) #We search the db for the note with that id as primary key, because .query.get searches by default primary keys
    if note: #If there is a matching note
        if note.user_id == current_user.id: #If the signed in user owns this note
            db.session.delete(note) 
            db.session.commit()       
    return jsonify({}) #In the end return an empty response, because we need to