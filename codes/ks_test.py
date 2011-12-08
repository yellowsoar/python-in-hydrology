# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 19:03:13 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import scipy.stats as st

x = np.random.randn(1000) # x is normal
y = np.random.rand(1000) # y is uniform

D, p = st.kstest(x,'norm')
print(p)

D, p = st.kstest(y,'norm')
print(p)


