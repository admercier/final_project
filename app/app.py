from flask import Flask, render_template, request, flash, redirect, url_for, session
#from flask_session import Session
#SESSION_TYPE = 'memcache'
import flask
import pandas as pd
import os
from os import path
import sys



# Create an instance of Flask app
app = Flask(__name__)
#sess = Session()
#my_resp = ""

@app.route('/index')
@app.route('/')
def index():
    #response = request.args['response']
    #response = session['response']
    if path.exists("response.txt"):
        file_r = open("response.txt","r+")
        response = file_r.read()
        file_r.close()
        os.remove("response.txt")
    else:
        response = "Please Input Information"
        print("no submit yet")

    return render_template('index.html', response = response)

import GPT2
@app.route('/Date_Input', methods=["GET","POST"]) 
def Date_Input():
    sex = request.form['sex']
    hair = request.form['hair']
    height = request.form['height']
    score = request.form['score']
    birth = request.form['birth']
    response = GPT2.Date_Input(sex,hair,height,score,birth)
    #session['response'] = response
    file_w = open("response.txt","w")
    file_w.writelines(response)
    file_w.close()
    return redirect(url_for('.index')) 
   

# @app.route('/my_resp', methods=['POST']) 
# def ml_input():
#      in_state = request.form['input_statement']
#      gpt.ml_input(in_state)
#      return render_template('index3.html') 

#@app.route('/ML_response/')
#def ML_response():
    #return render_template('index.html')

 
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    #app.secret_key = 'super secret key'
    #app.config['SESSION_TYPE'] = 'filesystem'

    #sess.init_app(app)
    app.run(debug = True)