
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
# as browser_session ????? 
from flask_debugtoolbar import DebugToolbarExtension
from script import userSearch
from model import connect_to_db, db


app = Flask(__name__)

app.secret_key = "ABC"

@app.route('/')
def index():
	"""Homepage."""

	return render_template("index.html")

@app.route('/search')
def search():
	"""This search returns Walmart API Search Items"""
	search = request.args.get('userSearch')
	results = userSearch(search)
	return jsonify(results)





if __name__ == "__main__":

	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)


	app.run()