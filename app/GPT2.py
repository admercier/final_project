import pandas as pd
from flask import Flask, render_template, request, flash, redirect, url_for
import json
import os
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import sys
#import model, sample, encoder
from src import model, sample, encoder

#sys.path.append('src/')
from src import interactive_conditional_samples as ics
from src import rene


def Date_Input(sex,hair,height,score,birth):
    

    if score == "yes" :
        score_var = "want to have sex with"
    else:
        score_var = "do not want to have sex with"


    input_statement = ("What do I say to my date who is a "+ sex + " who has " + hair + " hair, and is " + height + ". I " + score_var + " them. " + " Their birth sign is " + birth)
    response = ics.interact_model( model_name='1558M',nsamples=1,top_k=40,temperature=.80, input_statement = input_statement)
    #my_resp = rene.rene_test(input_statement)

    return response
  
