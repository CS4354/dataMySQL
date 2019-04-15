import logging

import pymysql
from flask import Flask, jsonify, request, make_response, abort

from models import States, Counties, Addresses, Pollutions

app = Flask("pollution_api")
connection = pymysql.connect(host="127.0.0.1", user="root", db="test", autocommit=True)
cur = db.cursor(pymysql.cursors.DictCursor)

@app.route("/<int:year>", methods=["GET"])
def year(year):
    """Return all pollution items for a given year"""
    # Look up year in database
    pass


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)