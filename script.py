from urllib2 import urlopen
import requests

api_key = "qb5mmbrawdsnnr74yqc6sn8q"


# May 12
# Need to find chicken meat categoryId to feed to Search API in order to
# find all human food chicken products on the walmart website


dict_of_product_ids = {}

def userSearch(searchTerm):
	"""This is the function that passes the user search term to the Walmart API"""	
	search_api = requests.get("http://api.walmartlabs.com/v1/search?query=" + searchTerm + "&format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q")
	searchApi = search_api.json()
	return searchApi

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