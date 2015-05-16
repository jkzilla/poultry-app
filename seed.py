
from model import Taxonomy, connect_to_db, db
from script_taxonomy import get_wm_taxonomy
from server import app
from pprint import pprint

DB_URI = "http:///taxonomy.db" 

get_taxonomy_json_object = get_wm_taxonomy()

def load_taxonomy():
	"""Load taxonomy from json object given by WM API."""
	get_taxonomy_json_object = get_wm_taxonomy()

	for k, v in get_taxonomy_json_object.items():
		if k:
			if k is not "children":
				print "hello"
		elif isinstance(k, list): 
			for item in load_taxonomy(v):
				print "goodbye"



# top level categories seeding
	# for category in get_taxonomy_json_object["categories"]:
	# 	children = False
	# 	pprint(category)
	# 	if category['children'] is not None:
	# 		children = True
	# 		# key: [{values}]
	# 	taxonomy_table_values = Taxonomy(children=children, category_node=category["id"], name=category["name"], path=category["path"])
	# 	db.session.add(taxonomy_table_values)
	# 	db.session.commit()

		
	# 	for child in category["children"]:
	# 		children = False
	# 		if child['children'] is not None:
	# 			children = True
	# 		# key: [{values}]
	# 		taxonomy_table_values = Taxonomy(children=children, category_node=child["id"], name=child["name"], path=child["path"])
	# 		db.session.add(taxonomy_table_values)
	# 		db.session.commit()


	# 		for grandchild in child["children"]:
	# 			children = False
	# 			if grandchild["children"] is not None:
	# 				children = True
	# 				print "Grandchild had a child! Grandchild at %s" % (grandchild["name"])
	# 			taxonomy_table_values = Taxonomy(children=children, category_node=grandchild["id"], name=grandchild["name"], path=grandchild["path"])
	# 			db.session.add(taxonomy_table_values)
	# 			db.session.commit()

# this returns a json object 
# key: [{this is an array of dicts}]
			# key: value
			# key: value
			# key: value
			# children: [{this is an array of dicts}]
			# 		key: value
			# 		key: value
			# 		key: [{this is an array of dicts}]
			# key: value
			# key: value
			# key: [{this is an array of dicts}]

if __name__ == "__main__":
    connect_to_db(app)
    load_taxonomy()