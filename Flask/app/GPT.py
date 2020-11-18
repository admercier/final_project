import pandas as pd
from flask import request
from flask import Flask 




def Date_Input(sex,hair,height,score,birth):
    
    if score == "yes" :
        score_var = "want to have sex with"
    else:
        score_var = "do not want to have sex with"


input_statement = ("I am on a date with a {sex} who has {hair} hair and is {height}.  I definitly {score_var} them.  My date is also a {birth}")


  
