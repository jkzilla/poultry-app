


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
	brand_name_list = [

		{"brand_name": "Great Value",
		"parent_company": None,
		"brand_website": "http://www.walmart.com/",
		"brand_youtube": "https://www.youtube.com/user/Walmart",
		"brand_instagram": "http://instagram.com/walmart",
		"brand_facebook": "https://www.facebook.com/walmart?fref=nf",
		"brand_twitter": "https://twitter.com/Walmart?",
		"brand_google_plus": "http://google.com/+Walmart",
		"brand_pintrest": "https://www.pinterest.com/walmart/",
		"brand_conventional": True,
		"brand_organic": False,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		},
		{"brand_name": "Tyson",
		"parent_company": None,
		"brand_website": "http://www.tysonfoods.com/",
		"brand_youtube": "https://www.youtube.com/user/TysonCommunity",
		"brand_instagram": "https://instagram.com/tysonfoods/",
		"brand_facebook": "https://www.facebook.com/TysonFoods",
		"brand_twitter": "https://twitter.com/tysonfoods",
		"brand_google_plus": "https://plus.google.com/wm/1/+tysonfoods/posts",	
		"brand_pintrest": "https://www.pinterest.com/TysonFoods/",
		"brand_conventional": True,
		"brand_organic": False,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		},

		{"brand_name": "Swansom",
		"parent_company": None,
		"brand_website": "http://www.swansonchicken.com/",
		"brand_youtube": "https://www.youtube.com/user/SwansonChicken",
		"brand_instagram": "https://instagram.com/swansonbroths/",
		"brand_facebook": "https://www.facebook.com/Swanson",
		"brand_twitter": "https://twitter.com/swansonchicken",
		"brand_google_plus": None,
		"brand_pintrest": None,
		"brand_conventional": True,
		"brand_organic": False,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		}, 
		{"brand_name": "Valley Fresh",
		"parent_company": "Hormel",
		"brand_website": "www.valleyfresh.com/",
		"brand_youtube": "https://www.youtube.com/channel/UCf25ENy1sRMV-Jm-YgV4LUA",
		"brand_instagram": None,
		"brand_facebook": None,
		"brand_twitter": "https://twitter.com/hormelfoods",
		"brand_google_plus": "https://plus.google.com/110089461772215972543",
		"brand_pintrest": None,
		"brand_conventional": True,
		"brand_organic": True,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		},
		{"brand_name": "Hormel",
		"parent_company": None,
		"brand_website": "http://www.hormel.com/",
		"brand_youtube": "https://www.youtube.com/user/HormelFoodsCorp",
		"brand_instagram": "https://instagram.com/hormelfoods",
		"brand_facebook": "https://www.facebook.com/Hormelrecipeasy",
		"brand_twitter": "https://twitter.com/hormelfoods",
		"brand_pintrest": "https://www.pinterest.com/recipeasyhormel/",
		"brand_google_plus": "https://plus.google.com/110089461772215972543",
		"brand_conventional": True,
		"brand_organic": False,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		},
		{"brand_name": "Applegate",
		"parent_company": "Hormel",
		"brand_website": "http://www.applegate.com/",
		"brand_youtube": "https://www.youtube.com/user/ApplegateFarms",
		"brand_instagram": "http://instagram.com/applegate",
		"brand_facebook": "https://www.facebook.com/applegate",
		"brand_twitter": "https://twitter.com/Applegate",
		"brand_pintrest": "http://www.pinterest.com/applegatefarms/",
		"brand_google_plus": None,
		"brand_conventional": True,
		"brand_organic": True,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		},
		{"brand_name": "Perdue",
		"parent_company": None,
		"brand_website": "http://www.perdue.com/",
		"brand_youtube": "https://www.youtube.com/user/PerdueChicken",
		"brand_instagram": "https://instagram.com/p/vgdgfxRYTc/",
		"brand_facebook": "https://www.facebook.com/PerdueChicken",
		"brand_twitter": "https://twitter.com/perduechicken",
		"brand_google_plus": "https://plus.google.com/+perduechicken",
		"brand_pintrest": None,
		"brand_conventional": True,
		"brand_organic": False,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		},
		{"brand_name": "Banquet",
		"parent_company": "Con Agra Foods",
		"brand_website": "www.banquet.com/",
		"brand_youtube": "https://www.youtube.com/user/FoodYouLove",
		"brand_instagram": "https://instagram.com/conagrafoods/",
		"brand_facebook": "https://www.facebook.com/ConAgraFoods",
		"brand_twitter": "https://twitter.com/conagrafoods",
		"brand_google_plus": "https://plus.google.com/101514143380306398233/about",
		"brand_pintrest": None,
		"brand_conventional": True,
		"brand_organic": False,
 		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		},
		{"brand_name": "Foster Farms",
		"parent_company": None,
		"brand_website": "www.fosterfarms.com/",
		"brand_youtube": "https://www.youtube.com/user/FosterFarmsBrand",
		"brand_instagram": None,
		"brand_facebook": "https://www.facebook.com/FosterFarms",
		"brand_twitter": "https://twitter.com/ffchicken",
		"brand_google_plus": "https://plus.google.com/110873023933925073919/about",
		"brand_pintrest": None,
		"brand_conventional": True,
		"brand_organic": True,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		},
		{"brand_name": "Harvestland",
		"parent_company": "Perdue",
		"brand_website": "http://www.perdue.com/",
		"brand_youtube": "https://www.youtube.com/user/PerdueChicken",
		"brand_instagram": "https://instagram.com/p/vgdgfxRYTc/",
		"brand_facebook": "https://www.facebook.com/PerdueChicken",
		"brand_twitter": "https://twitter.com/perduechicken",
		"brand_google_plus": "https://plus.google.com/+perduechicken",
		"brand_pintrest": None,
		"brand_conventional": True,
		"brand_organic": True,
		"brand_free_range": False,
		"brand_pastured": False,
		"slow_growth": False,
		}, 
		]
	another_list = []
	for dict_item in brand_name_list:
			
		brand_table_values = Brand(	
		brand_name = dict_item['brand_name'],
		parent_company = dict_item['parent_company'],
		brand_website = dict_item['brand_website'],
		brand_youtube = dict_item['brand_youtube'],
		brand_instagram = dict_item['brand_instagram'],
		brand_twitter = dict_item['brand_twitter'],
		brand_pintrest = dict_item['brand_pintrest'],
		brand_google_plus = dict_item['brand_google_plus'],
		brand_conventional = dict_item['brand_conventional'],
		brand_organic = dict_item['brand_organic'],
		brand_free_range = dict_item['brand_free_range'],
		brand_pastured = dict_item['brand_pastured'],
		brand_slow_growth = dict_item['slow_growth'])
		db.session.add(brand_table_values)

	db.session.commit()
	# print type(brand_table_values) this is a class model.Brand
	
if __name__ == '__main__':
	from server import app
	connect_to_db(app)
	print "Connected to DB."
	seed_brand_info()