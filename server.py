
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
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

	"""This shows the results of search on search page. Working here May 24th. """
	user_query = request.args.get("search")
	# print user_query

	search_items_not_filtered_list = user_search(user_query)
	item_stuff_dict = {}
	i = 0
	# name = item_stuff_dict[item[u'name']]
	print item_stuff_dict
	for item in search_items_not_filtered_list:
		# search_items_not_filtered_list is a list of dicts 
		# print type(item) ==> this is dict
		# print type(search_items_not_filtered_list) this is a list
		print item[u'categoryNode']
		# print item[u'categoryNode'] => this prints a categoryNode in the terminal
		Taxonomy_obj = db.session.query(Taxonomy).filter(Taxonomy.path.like("%Food%")).filter_by(category_node=item[u'categoryNode']).all()
		# print type(Taxonomy_obj) this is a list 
		for obj in Taxonomy_obj:
			# print item[u'categoryNode'] => this prints category nodes such as 976759_976796_1001442, for canned chicken search this returned 9
			# print item[u'shortDescription']
			# print item_stuff_dictd[item[u'name']] 
			if item[u'categoryNode'] == obj.category_node:
				# here i am trying to assign name, category, sale_price, description, customer_rating_img to 
				# item_stuff_dict[item[u'name']] but i need to assigned to item_stuff_dict not item_stuff_dict[item[u'name']]
				item_stuff_dict['item_'+str(i)] = {
					"name": item.get(u'name', ""), 
					"item_id": item.get(u'itemId', ""),
					"category": item.get(u'categoryPath', ""), 
					"sale_price": item.get(u'salePrice', ""), 
					"description": item.get(u'shortDescription', ""), 
					# when I run server.py I receive a KeyError: u'ShortDescription'
					"customer_rating_img": item.get(u'customerRatingImage', "")
					}
				i+=1
					
	return render_template("searchresults.html", item_stuff_dict=item_stuff_dict)

#make a route with the lookup api
@app.route('/lookup_api', methods=['GET'])
def lookup_api():
	find_product = request.args.get("itemId");
	print find_product
	return 'hi'


if __name__ == "__main__":

	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)


	app.run()