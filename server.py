
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Taxonomy, Brand
from jinja2 import StrictUndefined
from utils import user_search
import requests


app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Homepage."""
	user = None
	return render_template("index.html", user=user)

@app.route('/login', methods=['POST'])
def login():
	"""User writes info in login email/pw boxes and clicks submit, which directs here"""
	email = request.form.get("email")
	password = request.form.get("password")
	user = User.query.filter_by(email=email, password=password).first()

	if user:
		flash("You are now logged in")
		db.session(email, password, user)
		return render_template("/nowsearch.html", user=user) 
	elif ValueError:
		flash("Invalid Login, please try again or register using the registration button below")
		return render_template("/index.html")

@app.route('/register', methods=['GET'])
def send_to_regist():
	"""Sends user to registration"""
	user = None
	return render_template("/registration.html", user=user)


@app.route('/submitregistrationtodb', methods=['POST'])
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
		return render_template("/nowsearch.html", user=user)

@app.route('/search')
def search_walmart():
	"""This search returns Walmart API Search Items"""
	search_wm_items = request.args.get('search')
	results = user_search(search)
	json_results = jsonify(results)
	return json_results

@app.route('/getresults', methods=['GET'])
def show_results():

	"""This shows the results of search on search page. Working here May 31th. """
	preferences = { 
		"preference1": "I prefer the least expensive option, always.",
		"preference2": "I buy organic products.",
		"preference3": "If I see a good cause, I support it.",
		"preference4": "I trust the market to give the consumer a satisfactory product",
		"preference5": "I have recently changed my diet and have started eating healthier.",
		"preference6": "I live by a budget.",
		"preference7": "I am afraid of what is sold in our grocery stores.",
		"preference8": "I was recently promoted.",
		"preference9": "I am buying for a celebration.",
		"preference10": "I always pay more for quality.",
		}
	user_query = request.args.get("search")
	user = session.get("name")
	# print user_query

	search_items_not_filtered_list = user_search(user_query)
	found_items = []
	
	# name = item_stuff_dict[item[u'name']]
	# print item_stuff_dict
	for item in search_items_not_filtered_list:
		# search_items_not_filtered_list is a list of dicts 
		# print type(item) ==> this is dict
		# print type(search_items_not_filtered_list) this is a list
		# print item[u'categoryNode']
		# print item[u'categoryNode'] => this prints a categoryNode in the terminal
		Taxonomy_obj = db.session.query(Taxonomy).filter(Taxonomy.path.like("%Food%")).filter_by(category_node=item[u'categoryNode']).all()
		# print Taxonomy_obj 
		# this is a list 
		for obj in Taxonomy_obj:
			# print item[u'categoryNode'] => this prints category nodes such as 976759_976796_1001442, for canned chicken search this returned 9
			print obj
			if item[u'categoryNode'] == obj.category_node:
				# here i am trying to assign name, category, sale_price, description, customer_rating_img to 
				# item_stuff_dict[item[u'name']] but i need to assigned to item_stuff_dict not item_stuff_dict[item[u'name']]
				found_items.append[{
					"name": item.get(u'name', ""), 
					"item_id": item.get(u'itemId', ""),
					"category": item.get(u'categoryPath', ""), 
					"sale_price": item.get(u'salePrice', ""), 
					"description": item.get(u'shortDescription', ""), 
					# when I run server.py I receive a KeyError: u'ShortDescription'
					"customer_rating_img": item.get(u'customerRatingImage', ""),
					"thumbnail_image": item.get(u'thumbnailImage', "")
					}]

	# print found	
	# [(2.50, 'green', 'dsd sdsd'), (3.50, 'red', '34343')]
	# [{'price': 2.50, 'color': 'red'}]			
	return render_template("searchresults.html", found_items=found_items, preferences=preferences, user=user)

#make a route with the lookup api. This route takes the item[item_id] from searchresults.html, and passes it
# to the lookup ap
@app.route('/brand-detail/<item_id>', methods=['GET'])
def lookup_api(item_id):
	# get item id from HTTP address
	# print item_id
	# # passes item id to lookup api
	product_wm_api = requests.get('http://api.walmartlabs.com/v1/items/' + item_id + '?format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q')
	# # creates json object
	product_info = product_wm_api.json()
	# returns brandName of product info in json object
	item_brand = product_info['brandName']
	# print item_brand this prints out as Great Value
	# print type(item_brand) this is a unicode object
	# takes brandName, accesses 'brands' table 
	brand_info = db.session.query(Brand).filter_by(brand_name=item_brand).first()
# if you search for a breand you dont find, make condition to show that it doesn't have info
# make template
	print brand_info
	brand_name = brand_info[0]

	return render_template('/brand-detail.html', brand_name=brand_name)

@app.route('/product_approval', methods=['GET'])
def get_purchase_y_n():
	yes1 = request.args.get("yes1")
	print yes1
	return render_template("/user_input.html", purchase_decision=yes)

@app.route('/user_input', methods=['GET'])
def get_user_input():
	return render_template("/nowsearch.html")

@app.route('/user_profile', methods=['GET'])
def go_to_user_profile():

	if 'email' not in session:
		return render_template("/index.html")

	name = db.session.query(User).filter_by(session["name"=name]).all()
	return render_template("user_profile/<name>.html", name=name)

@app.route('/logout')
def logout():
	logout_user()
	return render_template("/index.html")


if __name__ == "__main__":
	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)


	app.run()