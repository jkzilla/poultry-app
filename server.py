
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
from werkzeug.utils import unescape
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Taxonomy, Brand, SearchActivity, PurchaseActivity
from jinja2 import StrictUndefined
from utils import user_search
from datetime import datetime
import requests
from random import shuffle
from sqlalchemy import func
from bs4 import BeautifulSoup
import urllib2

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	"""Homepage."""
	print session
	return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
	"""User writes info in login email/pw boxes and clicks submit, which directs here"""
	email = request.form.get("email")
	password = request.form.get("password")
	user = User.query.filter_by(email=email, password=password).first()

	if user:
		session["user_id"] = user.user_id
		# print user.user_id
		flash("Welcome, %s" % user.name)
		

		return render_template("/nowsearch.html", user=user) 
	elif ValueError:
		flash("Invalid Login, please try again or register using the registration button below")
		return render_template("/index.html")

@app.route('/nowsearch', methods=['GET'])
def go_to_search():
	"""Sends user to search"""
	user_id = session.get("user_id")
	user = User.query.filter_by(user_id=user_id).first()

	return render_template("/nowsearch.html", user=user)


@app.route('/dashboard', methods=['GET'])
def go_to_dashboard():
	"""Sends user to dashboard"""
	return render_template("/dashboard.html")

@app.route('/register', methods=['GET'])
def send_to_regist():
	"""Sends user to registration"""
	return render_template("/registration.html")

@app.route('/dashboard')
def send_to_dashboard():
	"""Sends user to dashboard"""
	# purchased and conventional
	purchase_activity_conv = db.session.query(PurchaseActivity).filter_by(purchased=True, conventional=True).all()
	# purchased and organic
	purchase_activity_organic = db.session.query(PurchaseActivity).filter_by(purchased=True, organic=True).all()
	# search activity 
	search_activity = db.session.query(SearchActivity).all()

	# plot search_activity over time and purchase_activity over time

	list_of_dict = []


	data = {}
	datasets_dict = {}
	datasets_dict['label'] = "Search Activity, Items Purchased over Time"
	datasets_dict['fillColor'] = "rgba(220,220,220,0.5)"
	datasets_dict['strokeColor'] = "rgba(220,220,220,0.8)"
	datasets_dict['highlightFill'] = "rgba(220,220,220,0.75)"
	datasets_dict['highlightStroke'] = "rgba(220,220,220,1)"
	datasets_dict['data'] =search_activity, purchase_activity_organic, purchase_activity_conv
	data['labels'] = time
	data['datasets'] = [datasets_dict]
 

	list_of_dict.append(data)
	print list_of_dict 	

	return render_template("/dashboard.html")


@app.route('/submitregistrationtodb', methods=['POST'])
def post_reg_info_to_db():
	"""This saves the new user registration information in the db"""
	
	name = request.form.get("firstname")
	email = request.form.get("email")
	password = request.form.get("password")
	gender = request.form.get("gender")
	halal = request.form.get("halal")
	free_range = request.form.get("free_range")
	slow_growth = request.form.get("slow_growth")
	pastured = request.form.get("pastured")
	non_gmo = request.form.get("non_gmo")
	antibiotics = request.form.get("antibiotics")
	organic_100 = request.form.get("organic")
	organic_95 = request.form.get("organic_95")
	price = request.form.get("price")

	user_table_values = User(name=name, email=email, password=password, gender=gender, halal=halal, free_range=free_range, slow_growth=slow_growth, pastured=pastured, non_gmo=non_gmo, antibiotics=antibiotics, organic_100=organic_100, organic_95=organic_95, price=price)
	db.session.add(user_table_values)

	db.session.commit()

	# print user_table_values.user_id
	session["user_id"] = user_table_values.user_id
	
	if user_table_values:
		print name
		flash("Welcome, %s" % (name)) 
		return render_template("/nowsearch.html", user=user_table_values)

@app.route('/getresults', methods=['GET'])
def show_results():

	"""This shows the results of search on search page. Working here May 31th. """

	user_query = request.args.get("search")
	search_activity = SearchActivity(user_id=session.get('user_id'), search_query=user_query, datetime = datetime.now())

	db.session.add(search_activity)
	db.session.commit()
	search_items_not_filtered_list = user_search(user_query)
	found_items = []
	
	for item in search_items_not_filtered_list:
		Taxonomy_obj = db.session.query(Taxonomy).filter(Taxonomy.path.like("%Food%")).filter_by(category_node=item[u'categoryNode']).all()
		for obj in Taxonomy_obj:
			if item[u'categoryNode'] == obj.category_node:	
				found_items.append({
					"name": item.get(u'name', ""), 
					"item_id": item.get(u'itemId', ""),
					"category": item.get(u'categoryPath', ""), 
					"sale_price": format(item.get(u'salePrice', ""), ".2f"), 
					"description": unescape(item.get(u'shortDescription', "")), 
					"customer_rating_img": item.get(u'customerRatingImage', ""),
					"thumbnail_image": item.get(u'thumbnailImage', "")
					})
				
	return render_template("searchresults.html", found_items=found_items)

@app.route('/brand-detail/<item_id>', methods=['GET'])
def lookup_api(item_id):

	# # passes item id to lookup api
	product_wm_api = requests.get('http://api.walmartlabs.com/v1/items/' + item_id + '?format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q')

	session["item_id"] = item_id

	product_info = product_wm_api.json()
	print product_info
	
	# returns brandName of product info in json object
	item_brand = product_info['brandName']

	# print item_brand this prints out as Great Value

	# print type(item_brand) this is a unicode object

	# takes brandName, accesses 'brands' table 
	brand_info = db.session.query(Brand).filter_by(brand_name=item_brand).first()

		# if you search for a brand you dont find, make condition to show that it doesn't have info
	# except AttributeError:
	# 	flash("Please contact your local Walmart and ask this brand to participate in our program!")		
	session['conventional'] = brand_info.brand_conventional 
	session['organic'] = brand_info.brand_organic
	session['free_range'] = brand_info.brand_free_range
	session['pastured'] = brand_info.brand_pastured

	# opening wiki

	url = "http://en.wikipedia.org/wiki/Poultry_farming"
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]

	poultry_wiki_resource = opener.open(url)

	poultry_wiki_data = poultry_wiki_resource.read()
	poultry_wiki_resource.close()
	# Begin BeautifulSoup and Wikipedia
	soup = BeautifulSoup(poultry_wiki_data)

	organic_farm_info = None

	conventional_farm_info = []
	title = soup.find('span', id="Meat-producing_chickens_-_husbandry_systems").parent
	print title
	title_conv = title.text.rstrip("[edit]")
	conventional_farm_info.append(title_conv)
	nextNode = title
	while True:
		nextNode = nextNode.next_sibling
		print nextNode
		try:
			tag_name = nextNode.name
		except AttributeError:
			tag_name = ""
		if tag_name == "p":
			conventional_farm_info.append(nextNode.text)
		elif tag_name == 'h2':
			break
	return render_template('/brand-detail.html', brand=brand_info, conventional_farm_info=conventional_farm_info, organic_farm_info=organic_farm_info)

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
	return redirect("/preference_questionnaire")

@app.route("/preference_questionnaire")
def get_user_session_answers():
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

	preferences_list_session_questions = []
	
	for key in keys:
		# this sets user.preference1, sqlalchemy will not take user.key with a key variable
		user_preference = getattr(user, key)
		
		# creating a list of the random preferences that were presented to the user during this particular session that will be saved to the session for access later
		session['pref'] = []
		# if the user has answered the question
		if user_preference:
			continue
		# if the user has not answered the question
		if not user_preference:
			# this appends, to the session list, the key, eg preference1, and the preferences[key], eg the string of the question, "I live by a budget." This is a list of every unanswered question
			preferences_list_session_questions.append((key, preferences[key]))
	# in order to create a random question set, the session preference are shuffled
	shuffle(preferences_list_session_questions)
	# and three or less questions are chosen, less if the user has answered most of the questions
	rand_questions = preferences_list_session_questions[:3]		
	
	for question in rand_questions:
		session['pref'].append(question[0])
	return render_template("/user_input.html", preferences_question_list=rand_questions)


@app.route('/add_preferences/<int:user_id>', methods=['POST'])
def add_user_preferences(user_id):

	user = db.session.query(User).filter_by(user_id=session["user_id"]).one()

	# take the information submited by the form for the preference questions
	session_prefs = session.get("pref")
	for pref in session_prefs:
		pref_score = request.form.get(pref)
		setattr(user, pref, pref_score)
	db.session.commit()

	search_activity = db.session.query(SearchActivity.search_query, func.count(SearchActivity.search_query)).group_by(SearchActivity.search_query).all()
	# print search_activity.search_query

	list_of_dict = []



	search_activity_two_lst = [[item_name.encode('ascii', 'ignore') for item_name, count in search_activity], [count for item_name, count in search_activity]]
	print search_activity_two_lst[0]
	print search_activity_two_lst[1]
	data = {}
	datasets_dict = {}
	datasets_dict['label'] = "Search Activity"
	datasets_dict['fillColor'] = "rgba(220,220,220,0.5)"
	datasets_dict['strokeColor'] = "rgba(220,220,220,0.8)"
	datasets_dict['highlightFill'] = "rgba(220,220,220,0.75)"
	datasets_dict['highlightStroke'] = "rgba(220,220,220,1)"
	datasets_dict['data'] =search_activity_two_lst[1]
	data['labels'] = search_activity_two_lst[0]
	data['datasets'] = [datasets_dict]
 

	list_of_dict.append(data)
	print list_of_dict 	

	return render_template('user_profile.html', user=user, data=data)

@app.route('/user_profile/<int:user_id>', methods=['GET'])
def go_to_user_profile(user_id):

	if 'user_id' not in session:
		return render_template("/index.html")
	# to go to the user profile you have to access the session user id and look that up in the db

	user_id = session.get("user_id")
	user = User.query.filter_by(user_id=user_id).first()
	print user
	search_activity = db.session.query(SearchActivity.search_query, func.count(SearchActivity.search_query)).group_by(SearchActivity.search_query).all()

	list_of_dict = []



	search_activity_two_lst = [[item_name.encode('ascii', 'ignore') for item_name, count in search_activity], [count for item_name, count in search_activity]]
	print search_activity_two_lst[0]
	print search_activity_two_lst[1]
	data = {}
	datasets_dict = {}
	datasets_dict['label'] = "Search Activity"
	datasets_dict['fillColor'] = "rgba(220,220,220,0.5)"
	datasets_dict['strokeColor'] = "rgba(220,220,220,0.8)"
	datasets_dict['highlightFill'] = "rgba(220,220,220,0.75)"
	datasets_dict['highlightStroke'] = "rgba(220,220,220,1)"
	datasets_dict['data'] =search_activity_two_lst[1]
	data['labels'] = search_activity_two_lst[0]
	data['datasets'] = [datasets_dict]
 

	list_of_dict.append(data)
	print list_of_dict 	

	return render_template("user_profile.html", user=user, data=data)

@app.route('/logout')
def logout():
	del session['user_id']

	return render_template("/index.html")


if __name__ == "__main__":
	app.debug = True

	connect_to_db(app)

	DebugToolbarExtension(app)


	app.run()