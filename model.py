"""Models and database functions for seeding my taxonomy database so
sorting through the walmart taxonomy is easier yay."""


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
		"""This is a helpful representation"""
		return "<Taxonomy category_node=%s name=%s>" % (self.category_node, self.name)  

	# if children:
		# import values

class User(db.Model):
	"""This is our fake user database"""

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	email = db.Column(db.String(64), nullable=False)
	password = db.Column(db.String(64), nullable=False)

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
	brand_instagram = db.Column(db.String(64))
	brand_twitter = db.Column(db.String(64))
	brand_pintrest
	brand_google_plus = db.Column(db.String(64))
	brand_conventional = db.Column(db.Boolean)
	brand_organic = db.Column(db.Boolean)
	brand_free_range = db.Column(db.Boolean)
	brand_pastured = db.Column(db.Boolean)
	brand_slow_growth = db.Column(db.Boolean)



class UserPreferences(db.Model):
	"""These are our user preferences"""
	__tablename__ = "preferences"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	halal = db.Column(db.Boolean)
	free_range = db.Column(db.Boolean)
	slow_growth = db.Column(db.Boolean)
	pastured = db.Column(db.Boolean)
	non_gmo = db.Column
	antibiotics = db.Column(db.Boolean)
	organic_100 = db.Column(db.Boolean)
	organic_95 = db.Column(db.Boolean)
	price = db.Column(db.Boolean)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxonomy.db'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."