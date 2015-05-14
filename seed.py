
from model import show_taxonomy, connect_to_db, db
from script_taxonomy import get_wm_taxonomy
from server import app

DB_URI = http:///taxonomy.db 


def load_taxonomy():
	"""Load taxonomy from json object given by WM API."""
	get_taxonomy_json_object = get_wm_taxonomy()

	for key,value in get_wm_taxonomy:

		taxonomy_table_values = Taxonomy(categoryNode="id", )
		while children:


# this returns a json object 
# # key: [[array of dict]
# 			key: value
# 			key: value
			# key: value
# 			key: [array]
# 					key: value
# 					key: value
# 					key: [array]
# 			key: value
# 			key: value
# 			key: [array]

if __name__ == "__main__":
    connect_to_db(app)

    load_taxonomy()