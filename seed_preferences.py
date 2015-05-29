


from model import Brand, db, connect_to_db

import csv

DB_URI = "http:///taxonomy.db" 


def seed_brand_info():

	"""This is where we create the brand database: 
	class Brand(db.Model):
	This the brand database for Walmart products in the category of Food:

	__tablename__ = "brands"

	brand_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	brand_name = db.Column(db.String(64), nullable=False)
	brand_website = db.Column(db.String(64), nullable=False)
	brand_youtube = db.Column(db.String(64))
	brand_instagram = db.Column(db.String(64))
	brand_twitter = db.Column(db.String(64))
	brand_google_plus = db.Column(db.String(64))
	brand_conventional = db.Column(db.Boolean)
	brand_organic = db.Column(db.Boolean)
	brand_free_range = db.Column(db.Boolean)
	brand_pastured = db.Column(db.Boolean) 

	as such"""

	# def __init__(self, brand_name, brand_website, brand_youtube, brand_instagram, 
	# 	brand_twitter, brand_google_plus, brand_conventional, brand_organic, brand_free_range, 
	# 	brand_pastured)
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

	preference_table_values = preferences(	
		preference1 = preferences.get('preference1'),
		preference2 = preferences.get('preference2')
		preference3 = preferences.get('preference3'),
		preference4 = preferences.get('preference4'),
		preference5 = preferences.get('preference5'),
		preference6 = preferences.get('preference6'),
		preference7 = preferences.get('preference7'),
		preference8 = preferences.get('preference8'),
		preference9 = preferences.get('preference9'),
		preference10 = preferences.get('preference10'))
		db.session.add(preference_table_values)

	db.session.commit()
	
if __name__ == '__main__':
	from server import app
	connect_to_db(app)
	print "Connected to DB."
	seed_preferences()