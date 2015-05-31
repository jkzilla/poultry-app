
from model import User, db, connect_to_db
import random
import csv

DB_URI = "http:///poultrywatch.db" 


def seed_users():
	"""This takes the .csv user data and seeds it into my database"""
	openfile = open("./data/Fake_user_data.csv")
	for line in openfile:
		user_row = line.rstrip().split(",")
		user_row[0] = user_row[0].replace('\xa0', ' ').rstrip()
		# print user_row
		user_table_values = User(
				name=user_row[0], 
				email=user_row[1], 
				password=user_row[3],
				gender=user_row[4],
				halal = None,
	free_range = random.randint(0,1),
	slow_growth = random.randint(0,1),
	pastured = random.randint(0,1),
	non_gmo = random.randint(0,1),
	antibiotics = random.randint(0,1),
	organic_100 = random.randint(0,1),
	organic_95 = random.randint(0,1),
	price = random.randint(0,5),
	preference1 = random.randint(0,5),
	preference2 = random.randint(0,5),
	preference3 = random.randint(0,5),
	preference4 = random.randint(0,5),
	preference5 = random.randint(0,5),
	preference6 = random.randint(0,5),
	preference7 = random.randint(0,5),
	preference8 = random.randint(0,5),
	preference9 = random.randint(0,5),
	preference10 = random.randint(0,5),

				)
		db.session.add(user_table_values)

	db.session.commit()


if __name__ == '__main__':
	from server import app
	connect_to_db(app)
	print "Connected to DB."
	seed_users()