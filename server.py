
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
# as browser_session ????? 
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Taxonomy
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
		flash("You are now logged in")
		return render_template("/nowsearch.html") 
	elif ValueError:
		flash("Invalid Login, please try again or register using the registration button below")
		return render_template("/index.html")

@app.route('/register', methods=['GET'])
def send_to_regist():
	"""Sends user to registration"""
	return render_template("/registration.html")
# WORKING HERE WORKING HERE WORKING HERE WORKING HERE
@app.route('/submitregistration', methods=['POST'])
def post_reg_info_to_db():
	"""This saves the new user registration information in the db"""
	
	name = request.form.get("firstname")
	email = request.form.get("email")
	password = request.form.get("password")

	user_table_values = User(name=name, email=email, password=password)
	db.session.add(user_table_values)

	db.session.commit()
	
	user = User.query.filter_by(email=email)
	if user:
		flash("You are now logged in")
		return render_template("/nowsearch.html")

@app.route('/search')
def search_walmart():
	"""This search returns Walmart API Search Items"""
	search_wm_items = request.args.get('search')
	results = user_search(search)
	json_results = jsonify(results)
	return json_results

@app.route('/getresults', methods=['GET'])
def show_results():

	"""This shows the results of search on search page"""
	user_query = request.args.get("search")
	# print user_query

	search_items_not_filtered_list = user_search(user_query)
	item_approved_list = []

	for item in search_items_not_filtered_list:
		Taxonomy_obj = db.session.query(Taxonomy).filter(Taxonomy.path.like("%Food%")).filter_by(category_node=item[u'categoryNode']).all()
		for obj in Taxonomy_obj:
			print obj.category_node
			if item[u'categoryNode'] == obj.category_node:
				item_stuff = item[u'name'], item[u'categoryPath'], item[u'salePrice'], item[u'shortDescription'], item[u'itemId'], item[u'addToCartUrl'], item[u'customerRatingImage']
				item_approved_list.append(item_stuff)
	return render_template("searchresults.html", item_approved_list=item_approved_list)


if __name__ == "__main__":

	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)


	app.run()