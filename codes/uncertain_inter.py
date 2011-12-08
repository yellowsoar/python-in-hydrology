# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:48:12 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# generate some data
x = 100*np.sin(np.linspace(0,10,100))
X = np.vstack([x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x])
e = 10*np.random.randn(20,100) 

X_err = X+e

plt.clf()
plt.plot(X_err.T, 'k')
plt.xlabel('Time')
plt.ylabel('X')
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/X_err.png')

ll = st.scoreatpercentile(X_err, 10)
ml = st.scoreatpercentile(X_err, 50)
ul = st.scoreatpercentile(X_err, 90)

plt.clf()
plt.plot(ml, 'g', lw=2, label='Median')
plt.plot(ul, '--m', label='90%')
plt.plot(ll, '--b', label='10%')
plt.xlabel('Time')
plt.ylabel('X')
plt.legend(loc='best')
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/X_uncer.png')

plt.clf()
plt.plot(ml, 'g', lw=2, label='Median')
plt.fill_between(range(100), ul, ll, color='k', alpha=0.4, label='90%')
plt.xlabel('Time')
plt.ylabel('X')
plt.legend(loc='best')
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/X_uncer_shade.png')



