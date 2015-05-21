from urllib2 import urlopen
import requests
import json
from pprint import pprint
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Taxonomy
from flask import Flask, render_template, redirect, request, flash, session, jsonify, json



api_key = "qb5mmbrawdsnnr74yqc6sn8q"


# May 12
# Need to find chicken meat categoryId to feed to Search API in order to
# find all human food chicken products on the walmart website


dict_of_product_ids = {}

def user_search(search_term):
	"""This is the function that passes the user search term to the Walmart API"""	
	search_api = requests.get("http://api.walmartlabs.com/v1/search?query=" + search_term + "&format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q")
	searchApi = search_api.json()
	search_items_not_filtered = searchApi['items']
	return search_items_not_filtered
	
def get_lookup(item_id):
	"""This connects to WM API Lookup and returns the single product that matches the item id that you provide. From where? Search API!
	How does the search API return all the products that I want that fall under the human food category Chicken (undetermined what WM calls it."""

	if categoryNode:
		r = urlopen('http://api.walmartlabs.com/v1/taxonomy?format=json&' + 'categoryId=' + categoryNode + "&" + 'apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
		taxonomy_dict = json.load(r)
	else: 
		print "I need a categoryNode"
	pprint(taxonomy_dict)

