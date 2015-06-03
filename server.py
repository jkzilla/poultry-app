
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Taxonomy, Brand, SearchActivity, PurchaseActivity
from jinja2 import StrictUndefined
from utils import user_search
from datetime import datetime
import requests
import random
# import simplejson
# import urllib2

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
		session["user_id"] = user.user_id
		print user.user_id
		flash("You are now logged in")
		

		return render_template("/nowsearch.html", user=user) 
	elif ValueError:
		flash("Invalid Login, please try again or register using the registration button below")
		return render_template("/index.html")

@app.route('/register', methods=['GET'])
def send_to_regist():
	"""Sends user to registration"""
	return render_template("/registration.html")


@app.route('/submitregistrationtodb', methods=['POST'])
def post_reg_info_to_db():
	"""This saves the new user registration information in the db"""
	
	name = request.form.get("firstname")
	email = request.form.get("email")
	password = request.form.get("password")

	user_table_values = User(name=name, email=email, password=password)
	db.session.add(user_table_values)

	db.session.commit()

	print user_table_values.user_id
	session["user_id"] = user_table_values.user_id
	
	if user_table_values:
		flash("You are now logged in")
		return render_template("/nowsearch.html", user=user_table_values)

# @app.route('/search')
# def search_walmart():
# 	"""This search returns Walmart API Search Items"""
# 	search_wm_items = request.args.get('search')



# 	results = user_search(search)
# 	json_results = jsonify(results)
# 	return json_results

@app.route('/getresults', methods=['GET'])
def show_results():

	"""This shows the results of search on search page. Working here May 31th. """

	user_query = request.args.get("search")
	# user = session.get("name")
	print user_query
	search_activity = SearchActivity(user_id=session.get('user_id'), search_query=user_query, datetime = datetime.now())

	db.session.add(search_activity)
	db.session.commit()
	print search_activity.query_id
	print search_activity.search_query
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
			# print obj
			print item[u'thumbnailImage']
			if item[u'categoryNode'] == obj.category_node:
				# here i am trying to assign name, category, sale_price, description, customer_rating_img to 
				# item_stuff_dict[item[u'name']] but i need to assigned to item_stuff_dict not item_stuff_dict[item[u'name']]
				found_items.append({
					"name": item.get(u'name', ""), 
					"item_id": item.get(u'itemId', ""),
					"category": item.get(u'categoryPath', ""), 
					"sale_price": item.get(u'salePrice', ""), 
					"description": item.get(u'shortDescription', ""), 
					# when I run server.py I receive a KeyError: u'ShortDescription'
					"customer_rating_img": item.get(u'customerRatingImage', ""),
					"thumbnail_image": item.get(u'thumbnailImage', "")
					})

	# print found	
	# [(2.50, 'green', 'dsd sdsd'), (3.50, 'red', '34343')]
	# [{'price': 2.50, 'color': 'red'}]			
	return render_template("searchresults.html", found_items=found_items)

#make a route with the lookup api. This route takes the item[item_id] from searchresults.html, and passes it
# to the lookup ap
@app.route('/brand-detail/<item_id>', methods=['GET'])
def lookup_api(item_id):
	# get item id from HTTP address
	# print item_id
	# # passes item id to lookup api
	product_wm_api = requests.get('http://api.walmartlabs.com/v1/items/' + item_id + '?format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q')
	session["item_id"] = item_id
	# # creates json object
	product_info = product_wm_api.json()
	# returns brandName of product info in json object
	item_brand = product_info['brandName']
	# print item_brand this prints out as Great Value
	# print type(item_brand) this is a unicode object
	# takes brandName, accesses 'brands' table 
	brand_info = db.session.query(Brand).filter_by(brand_name=item_brand).first()
# if you search for a brand you dont find, make condition to show that it doesn't have info

	print brand_info.brand_conventional
	session['conventional'] = brand_info.brand_conventional 
	session['organic'] = brand_info.brand_organic
	session['free_range'] = brand_info.brand_free_range
	session['pastured'] = brand_info.brand_pastured

	return render_template('/brand-detail.html', brand=brand_info)

@app.route('/product_approval', methods=['GET'])
def get_purchase_y_n():
	yes = request.args.get("yes")                                   
	no = request.args.get("no")
	if yes:
		purchased = 1
	else:
		purchased = 0
	purchase_activity = PurchaseActivity(
		user_id=session.get('user_id'), 
		item_id=session.get('item_id'), 
		datetime=datetime.now(), 
		purchased=purchased, 
		conventional=session.get('conventional'), 
		organic=session.get('organic'), 
		free_range=session.get('free_range'), 
		pastured=session.get('pastured')
		)
	db.session.add(purchase_activity)
	db.session.commit()
	
	preferences = { 
	"preference1": "I prefer the least expensive option, always.",
	"preference2": "I buy organic products.",
	"preference3": "If I see a good cause, I support it.",
	"preference4": "I trust the market to give the consumer a satisfactory product",
	"preference5": "I have recently changed my diet and have started eating healthier.",
	"preference6": "I live by a budget.",
	"preference7": "I am cautious of what is sold in our grocery stores.",
	"preference8": "I was recently promoted.",
	"preference9": "I am buying for a celebration.",
	"preference10": "I always pay more for quality.",
	}

	user = db.session.query(User).filter_by(user_id=session.get("user_id")).first()

	keys = ["preference1", "preference2", "preference3", "preference4", 
	"preference5", "preference6", "preference7", "preference8", "preference9", "preference10"]

	preferences_list = []
	for key in keys:
		user_preference = getattr(user, key)
		if len(preferences_list) < 3:
			if user_preference:
				pass
			else:
				preferences_list.append(preferences[key])
				if len(preferences_list) is 1:
					session["first_session_preference"] = key
					print "first_session_preference"
					print key
				if len(preferences_list) is 2:
					session["second_session_preference"] = key
					print "second_session_preference"
					print key
				if len(preferences_list) is 3:
					session["third_session_preference"] = key
					print "third_session_preference"
					print key
	print preferences_list

	return render_template("/user_input.html", purchased=purchased, 
		preference_1=preferences_list[0], preference_2=preferences_list[1], 
		preference_3=preferences_list[2])


@app.route('/user_profile/<int:user_id>', methods=['GET'])
def go_to_user_profile(user_id):

	if 'user_id' not in session:
		return render_template("/index.html")
	# to go to the user profile you have to access the session user id and look that up in the db

	user_id = session.get("user_id")
	user = User.query.filter_by(user_id=user_id).first()
	print user
	return render_template("user_profile.html", user=user)

@app.route('/add_preferences/<int:user_id>', methods=['GET'])
def add_user_preferences(user_id):
	# take the information submited by the form for the preference questions
	first_session_pref = session.get("first_session_preference")
	# print first_pref ==> "preference1"
	second_session_pref = session.get("second_session_preference")
	third_session_pref = session.get("third_session_preference")
	
	user = db.session.query(User).filter_by(user_id=session["user_id"]).one()

	# get the value input by name "Choice1" "Choice2" "Choice3"
	first_pref_data = request.args.get("Choice1")
	second_pref_data = request.args.get("Choice2")
	third_pref_data = request.args.get("Choice3")
	
	if first_session_pref == "preference1": 
		user.preference1 = first_pref_data
		user.preference2 = second_pref_data
		user.preference3 = third_pref_data

	if first_session_pref == "preference4":
		user.preference4 = first_pref_data
		user.preference5 = second_pref_data
		user.preference6 = third_pref_data

	if first_session_pref == "preference7":
		user.preference7 = first_pref_data
		user.preference8 = second_pref_data
		user.preference9 = third_pref_data

	if first_session_pref == "preference10":
		user.preference10 = first_pref_data

	db.session.add(user)
	db.session.commit()

	return render_template('/user_profile.html', user=user)

@app.route('/logout')
def logout():
	del session["user_id"]
	return render_template("/index.html")


if __name__ == "__main__":
	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)


	app.run()