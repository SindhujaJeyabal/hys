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
		return render_template('trips.html', name=username)
	else:
		return render_template('login.html')

@myapp.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=='POST':
		######## DELETE THIS PART FOR NUM. 3 ###########
		session['username'] = request.form['username']
		session['email'] = request.form['email']
		return redirect(url_for('index'))
		######## DELETE THIS PART FOR NUM. 3 ###########

@myapp.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@myapp.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
	username = ''
	if 'username' in session:
		username = escape(session['username'])
		return render_template('create.html', name=username)
	else:
		return render_template('login.html')

@myapp.route('/edit_trip', methods=['GET', 'POST'])
def edit_trip():
	return render_template('edit.html')

@myapp.route('/trips', methods=['GET'])
def viewtrips():
	if 'username' in session:
		return render_template('trips.html')
	else:
		return render_template('login.html')

@myapp.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
