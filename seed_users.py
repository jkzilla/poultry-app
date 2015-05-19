
from model import User, db

import csv

DB_URI = "http:///taxonomy.db" 


def seed_users():
	"""This takes the .csv user data and seeds it into my database"""

	# users = csv.reader('/data/fake_user_data.csv', delimiter=' ', quotechar='"')
	# print users
	# user_table_values = User(name=name, email=email, password=password)
	# db.session.add(taxonomy_table_values)

	# db.session.commit()


if __name__ == '__main__':
	from server import app
	connect_to_db(app)
	print "Connected to DB."
	get_wm_taxonomy()

