
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
# as browser_session ????? 
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User
from jinja2 import StrictUndefined
from utils import user_search

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
	user = User.query.filter_by(email=email, password=password).first()
	if user:
	# this needs to query the user.email object not the entire line of code
		flash("You are now logged in")
		return render_template("/nowsearch.html") 
	else:
		flash("Invalid Login, please try again or <a href='/registration.html'>register here</a>")

@app.route('/register')
def send_to_regist():
	"""Sends user to registration"""
	return render_template("/registration.html")


@app.route('/search')
def search_walmart():
	"""This search returns Walmart API Search Items"""
	search_wm_items = request.args.get('user_search')
	results = userSearch(search)
	json_results = jsonify(results)
	return json_results

@app.route('/getresults', methods=['GET'])
def show_results(user_query):
	"""This shows the results of search on search page"""
	search_items= user_search(user_query)
	return render_template("searchresults.html")




if __name__ == "__main__":

	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)


	app.run()