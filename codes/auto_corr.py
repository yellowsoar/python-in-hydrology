# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:38:43 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


x = 2*np.sin(np.arange(100)/10.0)
x += np.random.randn(len(x))

plt.clf()

plt.subplot(2,1,1)
plt.plot(x, '-s')
plt.ylabel('x', fontsize=20)
plt.grid(True)
plt.xlabel('Time')

plt.subplot(2,1,2)
c = plt.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
plt.grid(True)
plt.axhline(0, color='black', lw=2)
plt.axhline(1/np.exp(1), color='red')
plt.ylabel('Autocorrelation')
plt.xlim(xmin=0,xmax=100)
plt.xlabel('Lag')
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/corr_1.png')

lags = c[0]
auto_corr = c[1]
print(lags)
auto_corr = auto_corr[lags>=0]
lags = lags[lags>=0]
n = sum(auto_corr>np.exp(-1))
f = interp1d([auto_corr[n], auto_corr[n-1]], [lags[n], lags[n-1]])
corr_len = f(np.exp(-1))


#sp.interpolate.interp1d(x, y)

