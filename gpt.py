import os
os.chdir("gpt-2")

import json
import os
import numpy as np
import tensorflow as tf
import sys
import model, sample, encoder

src/interactive_conditional_samples.py --model_name='345M' --nsamples=2 --top_k=40 --temperature=.80