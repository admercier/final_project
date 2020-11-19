import json
import os
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import sys
import model, sample, encoder
#from src import model, sample, encoder

#sys.path.append('src/')
from src import interactive_conditional_samples as ics

ics.interact_model( model_name='1558M',nsamples=2,top_k=40,temperature=.80)
# 
# 
# --model_name='345M' --nsamples=2 --top_k=40 --temperature=.80