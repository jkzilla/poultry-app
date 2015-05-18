from urllib2 import urlopen
import urllib2
import requests
import json
from pprint import pprint
from model import Taxonomy, connect_to_db, db
from server import app
from pprint import pprint


api_key = "qb5mmbrawdsnnr74yqc6sn8q"

DB_URI = "http:///taxonomy.db" 


def get_wm_taxonomy():
	"""This connects to WM API taxonomy and returns the total list of taxonomy information for their database"""

	r = requests.get('http://api.walmartlabs.com/v1/taxonomy?format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
	taxonomy_dict = r.json()
	a = taxonomy_dict['categories']
	# a is a list object of dictionaries
	b = a
	recurse_keys(b)


def recurse_keys(b):
    for key in b:
		# if key in b:
		cat_id = b[0]['id']
		# print cat_id
		name = b[0]['name']
		path = b[0]['path']
		if isinstance(key, list):
			children = b[0]['children']
			# print children
		taxonomy_table_values = Taxonomy(children=True, category_node=cat_id, name=name, path=path)
		db.session.add(taxonomy_table_values)
		if isinstance(key, list):
			# for i in children:
			recurse_keys(children)
		db.session.commit()
# with open('taxonomy.json') as data_file:    
#     data = json.load(data_file)
#     a = data['categories']
#     recurse_keys(a)

#####################################################################################################################
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
	from server import app
	connect_to_db(app)
	print "Connected to DB."
	get_wm_taxonomy()