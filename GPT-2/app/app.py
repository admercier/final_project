from flask import Flask, render_template, request, flash, redirect, url_for
import flask
import pandas as pd
import os
import sys



# Create an instance of Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

import GPT2
@app.route('/Date_Input', methods=['POST']) 
def Date_Input():
    sex = request.form['sex']
    hair = request.form['hair']
    height = request.form['height']
    score = request.form['score']
    birth = request.form['birth']
    input_statement = GPT2.Date_Input(sex,hair,height,score,birth)
    return (url_for('/ml_input', input_statement = 'input_statement')) 
    


import gpt
@app.route('/ml_input', methods=['POST']) 
def ml_input():
    in_state = request.form['input_statement']
    gpt.ml_input(in_state)
    return render_template('index3.html') 

#@app.route('/ML_response/')
#def ML_response():
    #return render_template('index.html')

 
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)