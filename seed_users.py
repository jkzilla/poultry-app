
from model import User, db

import csv

DB_URI = "http:///taxonomy.db" 

print 
def seed_users():
	"""This takes the .csv user data and seeds it into my database"""
	anything = "anything"
	print "anything"
	return anything
	# users = csv.reader('/data/fake_user_data.csv', delimiter=' ', quotechar='"')
	# print users
	# user_table_values = User(name=name, email=email, password=password)
	# db.session.add(taxonomy_table_values)

	# db.session.commit()