# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:07:45 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from scipy.stats.mstats import chisquare
import numpy as np

f_obs = np.array([10, 15, 20, 30])
f_exp = np.array([10, 5, 15, 30])

c, p = chisquare(f_obs, f_exp)

print(c,p)