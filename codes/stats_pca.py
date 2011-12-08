# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:47:42 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

import matplotlib.mlab as ml
import numpy as np

mean = [0,0,0]
cov = [[1,0.2,0.5], [0.2,1,0.8], [0.5,0.8,1]]
print(np.array(cov))

data = np.random.multivariate_normal(mean,cov,100)

foo = ml.PCA(data)