#import fask
from flask import Flask, render_template, flash, request, redirect, session
#the 're' module will allow regular expression operations
import re
# create a regular expression object that we can run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z0]*$')
app = Flask(__name__)
app.secret_key = 'secret.key'
@app.route('/', methods=['GET'])
def index():
	return	render_template('index.html')

@app.route('/register', methods=['POST'])
def check_variable():	
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	password_confirmation = request.form['password_confirmation']

	#check variables
	error=False
	if len(request.form['first_name']) < 1:
		flash('Please Enter First Name.')
		error=True 
		return redirect('/')
	elif not NAME_REGEX.match(request.form['first_name']):
		flash('Letters only')
		error=True
	if len(request.form['last_name']) < 1:
		flash('Please Enter Last Name.')
		error=True
	elif not NAME_REGEX.match(request.form['last_name']):
		flash('Letters only')
		return redirect('/')
		error=True
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Please Enter Valid Email.')
		return redirect('/')
		error=True
	if len(request.form['password']) < 8:
		flash('Password must be at least 8 characters.')
		return redirect('/')
		error=True
	if request.form['password_confirmation']!= request.form['password_confirmation']:
		flash('Passwords does not match.')
		return redirect('/')
		error=True
	if error:
		return redirect('/')

	return render_template('register.html', first_name = first_name, last_name = last_name, email = email, password = password_confirmation)

app.run(debug=True)
