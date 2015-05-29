
from model import Manager, db, connect_to_db

import csv

DB_URI = "http:///poultrywatch.db" 


def seed_managers():
	"""This takes the .csv user data and seeds it into my database"""
	openfile = open("./data/Fake_user_data.csv")

	for line in openfile:
		user_row = line.rstrip().split(",")
		user_row[0] = user_row[0].replace('\xa0', ' ').rstrip()
		print user_row
		manager_table_values = Manager(name=user_row[0], email=user_row[1], password=user_row[3])
		db.session.add(manager_table_values)

	db.session.commit()


if __name__ == '__main__':
	from server import app
	connect_to_db(app)
	print "Connected to DB."
	seed_users()