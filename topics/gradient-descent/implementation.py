import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 
import seaborn as sns; sns.set()

import numpy as np
from numpy import linalg as LA
import pandas as pd

from sklearn import linear_model

# --------------- Helper Functions ---------------

def compute_mse(truth_vec, predict_vec):
    return np.mean((truth_vec - predict_vec)**2)
    
def compute_m_partial(in_vals, truth_vec, predict_vec):
    return -2*np.mean(in_vals*(truth_vec-predict_vec))

def compute_b_partial(truth_vec, predict_vec):
    return -2*np.mean(truth_vec-predict_vec)

def adjust_L(current_L, grad_step_num):
    if grad_step_num > 0 and grad_step_num % 10 == 0:
        return current_L * 0.8
    return current_L


# --------------- My Implementation ---------------

max_steps = 200
m = 0
b = 0
L = 0.01

# Set a tolerance for the smallest you will allow 
# the length of the gradient to be before stopping 
grad_tol = 0.01

outm = []
outb = []
outmse = []

for stp in range(max_steps):
    
    preds = m*neuro + b
    errormse = compute_mse(perform, preds)
    
    outm.append(m)
    outb.append(b)
    outmse.append(errormse)
    
    # 1. Computing the gradient
    d_m = compute_m_partial(neuro, perform, preds)
    d_b = compute_b_partial(perform, preds)
    
    norm_grad = np.linalg.norm([d_m, d_b])
    
    # If the length of the gradient is small enough, stop iterating
    if norm_grad < grad_tol:
        break
        
    m = m - (L*d_m)
    b = b - (L*d_b)
    
    L = adjust_L(L, stp)