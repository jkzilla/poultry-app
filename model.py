

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)



class Taxonomy(db.Model):
	"""          Taxonomy of Walmart Website

	 For this table, I am reading through the imported JSON object 
	 and identifying the
	 KEY 			- the unique nesting id
	 				which holds
	 		id      - nesting_id
	 		name    - the string that describes/holds key words for product seearch
	 		path	- more string desription holding key words for product seearch
	 		children : [ new array with further nested values to import to table]"""

	__tablename__ = "taxonomy" 

	nesting_id = db.Column(db.Integer, autoincrement=True, primary_key=True) 
	category_node = db.Column(db.String(64), nullable=False)
	name = db.Column(db.String(64), nullable=False)
	path = db.Column(db.String(64))
	children = db.Column(db.Boolean)


	def __repr__(self):
		"""This is a helpful representation."""
		return "<Taxonomy category_node=%s name=%s>" % (self.category_node, self.name)  

	# if children:
		# import values

class User(db.Model):
	"""This is our user database."""

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	email = db.Column(db.String(64), nullable=False)
	password = db.Column(db.String(64), nullable=False)
	gender = db.Column(db.String(64))


	halal = db.Column(db.Boolean)
	free_range = db.Column(db.Boolean)
	slow_growth = db.Column(db.Boolean)
	pastured = db.Column(db.Boolean)
	non_gmo = db.Column(db.Boolean)
	antibiotics = db.Column(db.Boolean)
	organic_100 = db.Column(db.Boolean)
	organic_95 = db.Column(db.Boolean)
	price = db.Column(db.Integer)
	preference1 = db.Column(db.Integer)
	preference2 = db.Column(db.Integer)
	preference3 = db.Column(db.Integer)
	preference4 = db.Column(db.Integer)
	preference5 = db.Column(db.Integer)
	preference6 = db.Column(db.Integer)
	preference7 = db.Column(db.Integer)
	preference8 = db.Column(db.Integer)
	preference9 = db.Column(db.Integer)
	preference10 = db.Column(db.Integer)	

	def __repr__(self):
		"""This is a helpful representation"""
		return "<User name=%s email=%s>" % (self.name, self.email)

class Brand(db.Model):
	"""This the brand database for Walmart products in the category of Food: """

	__tablename__ = "brands"

	brand_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	brand_name = db.Column(db.String(64), nullable=False)
	parent_company = db.Column(db.String(64))
	brand_website = db.Column(db.String(64), nullable=False)
	brand_youtube = db.Column(db.String(64))
	brand_facebook = db.Column(db.String(64))
	brand_instagram = db.Column(db.String(64))
	brand_twitter = db.Column(db.String(64))
	brand_pintrest = db.Column(db.String(64))
	brand_google_plus = db.Column(db.String(64))
	brand_conventional = db.Column(db.Boolean)
	brand_organic = db.Column(db.Boolean)
	brand_free_range = db.Column(db.Boolean)
	brand_pastured = db.Column(db.Boolean)
	brand_slow_growth = db.Column(db.Boolean)

class SearchActivity(db.Model):
	"""Database for user search activity"""

	__tablename__ = "search_activity"

	query_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id = db.Column(db.Integer, nullable=False)
	search_query = db.Column(db.String(64), nullable=False)
	datetime = db.Column(db.DateTime)

class PurchaseActivity(db.Model):
	"""Database for user purchase activity"""

	__tablename__ = "purchases"

	purchase_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id	= db.Column(db.Integer, db.ForeignKey('users.user_id'))
	item_id = db.Column(db.Integer, nullable=False)
	datetime = db.Column(db.DateTime)
	purchased = db.Column(db.Boolean)
	conventional = db.Column(db.Boolean)
	organic = db.Column(db.Boolean)
	free_range = db.Column(db.Boolean)
	pastured = db.Column(db.Boolean)

	user = db.relationship("User", backref=db.backref("purchases"))
# class Activity(db.Model):
	
# 	__tablename__ = "activities"

# 	activity_key = 
# 	user_id = db

class Product(db.Model):
	"""Our database of Walmart products that our users have scored and rated."""

	__tablename__ = "products"

	product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	
	# product_info =

class Rating(db.Model):
	"""Rating on individual chicken products that are associated with a Brand 
	in the Brand table."""

	__tablename__ = "ratings"

	rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	movie_id = db.Column(db.Integer, db.ForeignKey('brands.brand_id'))
	user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
	score = db.Column(db.Integer)

	user = db.relationship("User", backref="ratings")

	brand = db.relationship("Brand", backref=db.backref("ratings", order_by=rating_id))

	def __repr__(self):
		"""This is a helpful representation."""
		return "<Rating rating_id=%s product_id=%s user_id=%s score=%s" % (self.rating_id, self.product_id, self.user_id, self.score)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poultrywatch.db'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."