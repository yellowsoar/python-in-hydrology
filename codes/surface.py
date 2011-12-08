# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:43:04 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin

# define the variables
n = 0.015
S0 = 0.025
Q = 9.26
B = 2

# define the flow function
def flow(y):
    Q_estiamted = (1.49/n)*(S0**0.5)*((B*y)**(5/3))/((B+y)**(2/3))
    epsilon = np.abs(Q_estiamted - Q)
    return epsilon

y_optimum = fmin(flow,0.5)
print(y_optimum)