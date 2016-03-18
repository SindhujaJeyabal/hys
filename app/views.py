from app import myapp,model
from flask import request, render_template, session, redirect, url_for, escape
import os
import model

myapp.secret_key = os.urandom(24)

@myapp.route('/')
@myapp.route('/index')
def index():
	username = ''
	if 'username' in session:
		username = escape(session['username'])
		trips = model.get_user_trips(username)
		return render_template('trips.html', name=username, trips=trips)
	else:
		return render_template('login.html')

@myapp.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=='POST':
		######## DELETE THIS PART FOR NUM. 3 ###########
		session['username'] = request.form['username']
		session['email'] = request.form['email']
		model.add_user(session['username'])
		return redirect(url_for('index'))
		######## DELETE THIS PART FOR NUM. 3 ###########

@myapp.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@myapp.route('/trips', methods=['GET'])
def view_trips():
	print "viewing trips"
	if 'username' in session:
		username = session['username']
		trips = model.get_user_trips(username)
		return render_template('trips.html', name = username, trips = trips)
	else:
		return render_template('login.html')

@myapp.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
	username = ''
	if 'username' in session:
		if request.method == 'GET':
			username = escape(session['username'])
			return render_template('create.html', owner=username)
		elif request.method == 'POST':
			trip = dict()
			trip['trip_name'] = request.form.get('trip_name')
			trip['trip_owner'] = request.form.get('trip_owner')
			trip['participant_1'] = request.form.get('participant_1')
			trip['participant_2'] = request.form.get('participant_2')
			trip['destination_1'] = request.form.get('destination_1')
			model.add_trip(trip)
			return redirect(url_for('view_trips', name=username, trips = model.get_user_trips(username)))
	else:
		return render_template('login.html')

@myapp.route('/edit_trip', methods=['GET', 'POST'])
def edit_trip():
	return render_template('edit.html')

@myapp.route('/delete', methods=['GET'])
def delete_db():
	model.delete_all()
	return null

@myapp.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
