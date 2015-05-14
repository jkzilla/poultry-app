from urllib2 import urlopen
import requests
import json
from pprint import pprint


api_key = "qb5mmbrawdsnnr74yqc6sn8q"


def get_lookup(itemId):
	"""This connects to WM API Lookup and returns the single product that matches the item id that you provide. From where? Search API!
	How does the search API return all the products that I want that fall under the human food category Chicken (undetermined what WM calls it."""

	if categoryNode:
		r = urlopen('http://api.walmartlabs.com/v1/taxonomy?format=json&' + 'categoryId=' + categoryNode + "&" + 'apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
		taxonomy_dict = json.load(r)
	else: 
		print "I need a categoryNode"
	pprint(taxonomy_dict)
