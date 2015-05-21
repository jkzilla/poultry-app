from urllib2 import urlopen
import requests
import json
from pprint import pprint

from model import Taxonomy, db

api_key = "qb5mmbrawdsnnr74yqc6sn8q"


# May 12
# Need to find chicken meat categoryId to feed to Search API in order to
# find all human food chicken products on the walmart website


dict_of_product_ids = {}

def user_search(search_term):
	"""This is the function that passes the user search term to the Walmart API"""	
	search_api = requests.get("http://api.walmartlabs.com/v1/search?query=" + searchTerm + "&format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q")
	searchApi = search_api.json()
	for items in searchApi['items']:
		sql = db.session.query(Taxonomy).filter_by(category_node=items["categoryNode"]).one()
		print sql
	
def get_lookup(item_id):
	"""This connects to WM API Lookup and returns the single product that matches the item id that you provide. From where? Search API!
	How does the search API return all the products that I want that fall under the human food category Chicken (undetermined what WM calls it."""

	if categoryNode:
		r = urlopen('http://api.walmartlabs.com/v1/taxonomy?format=json&' + 'categoryId=' + categoryNode + "&" + 'apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
		taxonomy_dict = json.load(r)
	else: 
		print "I need a categoryNode"
	pprint(taxonomy_dict)




	# print body
# Lookup API

	# user chooses product using search api, 
	# pulls id from search api and provides lookup api info
# def showProductProfile():
# 	"""Get the full product info from the Lookup API."""

# 	Lookup_api = requests.get("http://api.walmartlabs.com/v1/items/" + "%d" 
# 	+ "?format=xml&apiKey=qb5mmbrawdsnnr74yqc6sn8q") % (
# 	# product_id
# 	) 

# 	response = Lookup_api.read()
# 	body = response
    
# 	print body

# product = requests.get('Lookup_api')


# def showProductRating():
# 	"""Get Walmart's user's reviews on this product."""

# 	Reviews_api = requests.get("http://api.walmartlabs.com/v1/reviews/" + "%d" 
# 	+ "?format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q") % (
# 	# product_id
# 	)

# def searchProductsMyUser():
# 	"""Search Walmart.com catalogue and return items available for sale.

# 	Query by string values."""
# 	search_api = requests.get("http://api.walmartlabs.com/v1/search?query=" 
# 		+ "%s" 
# 		+ "+%s"
# 		# how do add additional search terms?
# 		"&format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q")

# def searchProductsasDev():
# 	"""Search with categoryNode"""


# # Taxonomy API in script_taxonomy.py 