
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
# as browser_session ????? 
from flask_debugtoolbar import DebugToolbarExtension
from script import userSearch
from model import connect_to_db, db, User
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Homepage."""

	return render_template("index.html")

# not working
@app.route('/login', methods=['POST'])
def login():
	"""User writes info in login email/pw boxes and clicks submit, which directs here"""
	email = request.form.get("email")
	password = request.form.get("password")

	# this needs to query the user.email object not the entire line of code
	
	if email == User.query.get('email') and password == User.query.get('password'):
		if email in browser_session:
			browser_session['email'] = request.form['email']
			browser_session['password'] = request.form['password']
			flash("You are now logged in")
			return redirect("/nowsearch")
		else:
			print "LALALALA"
			flash("You are not logged in")

@app.route('/register')
def send_to_regist():
	"""Sends user to registration"""
	return render_template("/registration.html")

@app.route('/nowsearch')
def to_search():
	"""Sends to search page"""

	return render_template("searchpage.html")

@app.route('/search')
def search():
	"""This search returns Walmart API Search Items"""
	search = request.args.get('userSearch')
	results = userSearch(search)
	json_results = jsonify(results)
	return json_results

@app.route('/results')
def show_results(json_results):
	"""This shows the results of search on search page"""
	return render_template("searchresults.html")




if __name__ == "__main__":

	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)


	app.run()