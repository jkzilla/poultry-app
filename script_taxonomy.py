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
	# req = urllib2.Request('http://api.walmartlabs.com/v1/taxonomy?format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q')
	# for line in req[:10]:
	# 	print line 
	r = requests.get('http://api.walmartlabs.com/v1/taxonomy?format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
	taxonomy_dict = r.json()
	# print test
	a = taxonomy_dict['categories']
	# a is a list object of dictionaries
	b = a[0]
	# print b
	recurse_keys(b)


def recurse_keys(b):
    for key in b.keys():
        cat_id = b['id']
        name = b['name']
        path = b['path']
        print cat_id, name, path
#         if 'children' in key:
#         	children = True
#         # children: [{
# # 
#         # 
#         # }]
#         	recurse_keys(key['children'])
# 		taxonomy_table_values = Taxonomy(children=children, category_node=category["id"], name=category["name"], path=category["path"])
# 		db.session.add(taxonomy_table_values)
# 		db.session.commit()

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
	get_wm_taxonomy()