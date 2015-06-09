from urllib2 import urlopen
import requests
import json
from pprint import pprint
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Taxonomy
from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
from decimal import *


api_key = "qb5mmbrawdsnnr74yqc6sn8q"


dict_of_product_ids = {}



def user_search(search_term):
	"""This is the function that passes the user search term to the Walmart API"""	
	search_api = requests.get("http://api.walmartlabs.com/v1/search?query=" + search_term + "&format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q")
	# print "http://api.walmartlabs.com/v1/search?query=" + search_term + "&format=json&apiKey=qb5mmbrawdsnnr74yqc6sn8q"
	searchApi = search_api.json()
	# print searchApi['numItems']
	search_items_not_filtered = searchApi['items']
	return search_items_not_filtered
	
def get_lookup(item_id):
	"""This connects to WM API Lookup and returns the single product that matches the item id that you provide. From where? Search API!
	How does the search API return all the products that I want that fall under the human food category Chicken (undetermined what WM calls it."""

	if categoryNode:
		r = urlopen('http://api.walmartlabs.com/v1/taxonomy?format=json&' + 'categoryId=' + categoryNode + "&" + 'apiKey=qb5mmbrawdsnnr74yqc6sn8q') 
		taxonomy_dict = json.load(r)
	else: 
		print "I need a categoryNode"
	pprint(taxonomy_dict)

def moneyfmt(value, places=2, curr='', sep=',', dp='.',
             pos='', neg='-', trailneg=''):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = map(str, digits)
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))
# @app.route('/search')
# def search_walmart():
# 	"""This search returns Walmart API Search Items"""
# 	search_wm_items = request.args.get('search')



# 	results = user_search(search)
# 	json_results = jsonify(results)
# 	return json_results
