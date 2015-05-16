"""Models and database functions for seeding my taxonomy database so
sorting through the walmart taxonomy is easier yay."""


from flask_sqlalchemy import SQLAlchemy

"""THIS IS GETTING A RUNTIMEERROR: APPLICATION NOT REGISTERED ON DB INSTANCE AND NO APPLICATION TO 
CURRENT CONTEXT. SOMETHING ABOUT HOW I AM DEFINING DB?"""

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

	# if children:
		# import values





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