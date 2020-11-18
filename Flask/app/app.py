from flask import Flask, render_template, request, flash, redirect, url_for
import flask
import pandas as pd
import seaborn
from flask import request
from flask import Flask 
from flask import request 


# Create an instance of Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

import GPT
@app.route('/Date_Input', methods=['POST']) 
def Date_Input():
    sex = request.form['sex']
    hair = request.form['hair']
    height = request.form['height']
    score = request.form['score']
    birth = request.form['birth']
    GPT.Date_Input(sex,hair,height,score,birth)
    return ('/ml_input', "input_statement")                                                 

#import gpt2
#@app.route('/ml_input', methods=['POST']) 
#def ml_input():
 #   in_state = request.form['input_statement']
  #  gpt2.ml_input(in_state)
  #  return render_template('index2.html') 

#@app.route('/ML_response/')
#def ML_response():
    #return render_template('index.html')

 
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)