from flask import Flask, request, render_template, redirect, jsonify, url_for 
from flask_pymongo import PyMongo
from flask_assets import Environment, Bundle
from flask_scss import Scss
import pymongo
from datetime import datetime
from pymongo import MongoClient
from flask import jsonify, json, request
from bson.json_util import dumps
from bson.objectid import ObjectId
from dateutil.parser import parse
import sys
import numpy as np
import os
import csv

# Create an instance of Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#import gpt
#@app.route('/Date_input', methods=['POST']) 
#def Date(): 
   # ETL.Date_input(request)
    #return render_template('index.html')

#@app.route('/ML_response/')
#def ML_response():
    #return render_template('index.html')

 
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)