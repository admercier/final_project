import pandas as pd
from flask import request
from flask import Flask 




def Date_Input(sex,hair,height,score,birth):
    sex = request.form['sex']
    hair = request.form['hair']
    height = request.form['height']
    score = request.form['score']
    birth = request.form['birth']
    #input_statement = ""

    if score == "yes" :
        score_var = "want to have sex with"
    else:
        score_var = "do not want to have sex with"


    input_statement = ("I am on a date with a "+ sex + " who has " + hair + " hair, and is " + height + ". I " + score_var + " them. " + " Their birth sign is " + birth)

    #print (input_statement)
  
