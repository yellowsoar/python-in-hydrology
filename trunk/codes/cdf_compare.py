# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:16:29 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import scikits.statsmodels.api as sm
import matplotlib.pyplot as plt
import statistics

# generate some data
data = np.random.randn(100)

# estimate ecdf
ecdf = sm.tools.tools.ECDF(data)

# plot the ecdf using step function
plt.clf()
plt.step(ecdf.x, ecdf.y)
plt.xlabel('data', fontsize=20)
plt.ylabel('Empirical CDF', fontsize=15)
plt.savefig('/home/tomer/articles/python/tex/images/ecdf.png')

# evaluate value of ecdf at some data poing (say at 0)
print(ecdf(0))

# using kernels to estimate the pdf and cdf
y,x = statistics.cpdf(data, kernel = 'Epanechnikov') 

# plot the ecdf using step function
plt.clf()
plt.plot(ecdf.x, ecdf.y, label='Ordinary')
plt.plot(x, y, label='Kernel')
plt.xlabel('data', fontsize=20)
plt.ylabel('Empirical CDF', fontsize=15)
plt.legend(loc='best')
plt.savefig('/home/tomer/articles/python/tex/images/kernel.png')