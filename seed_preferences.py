


from model import User, db, connect_to_db

import csv

DB_URI = "http:///chickenwatch.db" 


def seed_more_user info():

	preferences = { 
		"preference1": "I prefer the least expensive option, always.",
		"preference2": "I buy organic products.",
		"preference3": "If I see a good cause, I support it.",
		"preference4": "I trust the market to give the consumer a satisfactory product",
		"preference5": "I have recently changed my diet and have started eating healthier.",
		"preference6": "I live by a budget.",
		"preference7": "I am afraid of what is sold in our grocery stores.",
		"preference8": "I was recently promoted.",
		"preference9": "I am buying for a celebration.",
		"preference10": "I always pay more for quality.",
		}

	user_table_values = User(	
		preference1 = preferences.get('preference1'),
		preference2 = preferences.get('preference2'),
		preference3 = preferences.get('preference3'),
		preference4 = preferences.get('preference4'),
		preference5 = preferences.get('preference5'),
		preference6 = preferences.get('preference6'),
		preference7 = preferences.get('preference7'),
		preference8 = preferences.get('preference8'),
		preference9 = preferences.get('preference9'),
		preference10 = preferences.get('preference10'))
	db.session.add(users_table_values)

	db.session.commit()
	
if __name__ == '__main__':
	from server import app
	connect_to_db(app)
	print "Connected to DB."
	seed_preferences()