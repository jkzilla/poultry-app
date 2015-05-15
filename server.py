
# from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session as browser_session
# from flask_debugtoolbar import DebugToolbarExtension

# from model import connect_to_db, db


app = Flask(__name__)

