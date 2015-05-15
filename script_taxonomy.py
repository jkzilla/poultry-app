from urllib2 import urlopen
import requests
import json
from pprint import pprint


api_key = "qb5mmbrawdsnnr74yqc6sn8q"


# Look for Walmart Python API Wrapper

dict_of_category_id = {}

def get_wm_taxonomy():
	"""This connects to WM API taxonomy and returns the total list of taxonomy information for their database, then flattens it to a non nested object"""

	# if categoryNode:
	r = urlopen('http://api.walmartlabs.com/v1/taxonomy?format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
	taxonomy_dict = json.load(r)
	# pprint(taxonomy_dict)
	return taxonomy_dict




# def get_wm_taxonomy(categoryNode):
# 	"""This connects to WM API taxonomy and returns the total list of taxonomy information for their database."""

# 	if categoryNode:
# 		r = urlopen('http://api.walmartlabs.com/v1/taxonomy?format=json&' + 'categoryId=' + categoryNode + "&" + 'apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
# 		taxonomy_dict = json.load(r)
# 	else: 
# 		print "I need a categoryNode"
# 	pprint(taxonomy_dict)


# def get_more_wm_taxonomy(taxonomy_dict):
# 	"""This takes the"""
# 	for category, list_of_walmart_categories in taxonomy_dict.items():
# 		print "This dictionary has one key, %s and many values, such as %s" % (category, list_of_walmart_categories[1]['name'])
# 	for category, list_of_walmart_dict in taxonomy_dict.items():
# 		print category, list_of_walmart_dict[1]['name']
			
# get_wm_taxonomy(str('3920_582106'))



if __name__ == '__main__':
	get_wm_taxonomy()