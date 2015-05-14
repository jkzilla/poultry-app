from urllib2 import urlopen
import requests
import json
from pprint import pprint


api_key = "qb5mmbrawdsnnr74yqc6sn8q"


# Look for Walmart Python API Wrapper

dict_of_category_id = {}

def get_wm_data(categoryNode):
	"""This connects to WM API taxonomy and returns the total list of taxonomy information for their database."""

	if categoryNode:
		r = urlopen('http://api.walmartlabs.com/v1/taxonomy?format=json&' + 'categoryId=' + categoryNode + "&" + 'apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
		taxonomy_dict = json.load(r)
	else: 
		print "I need a categoryNode"
	pprint(taxonomy_dict)



def get_more_wm_data(taxonomy_dict):
	"""This takes the"""
	for category, list_of_walmart_categories in taxonomy_dict.items():
		print "This dictionary has one key, %s and many values, such as %s" % (category, list_of_walmart_categories[1]['name'])
	for category, list_of_walmart_dict in taxonomy_dict.items():
		print category, list_of_walmart_dict[1]['name']
			


"""To use this, pass the best guess node you gained from your last call in order to sift down the data to the desired
	'Foods/Meats' and 'chicken' category (not sure if thats the taxonomy on human food (vs dog food) chicken items)
	This is the categoryId for Deli Meats:
                               'id': '976759_976789',
                               'name': 'Deli',
                               'path': 'Food/Deli'},

    This is the categoryId for 
	"""
get_wm_data(str('3920_582106'))



# if __name__ == '__main__':
# 	get_wm_data()