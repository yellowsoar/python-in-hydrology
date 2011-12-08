# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:43:28 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import scipy.interpolate

# generate data
x = np.linspace(0,1,5)
y = np.exp(-x)
f = sp.interpolate.interp1d(x, y)

xnew = np.linspace(x.min(), x.max())
ynew = f(xnew)   # use interpolation function returned by `interp1d`

plt.clf()
plt.plot(x, y, 'ro', label='y')
plt.plot(xnew, ynew, '-', label='ynew')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/inter.png')

x = np.random.rand(5)
y = np.random.rand(5)
pet = 2+2*np.random.rand(5)

rbfi = sp.interpolate.Rbf(x, y, pet)  # radial basis function interpolator instance

xi = np.linspace(0,1)
yi = np.linspace(0,1)
XI, YI = np.meshgrid(xi,yi)

di = rbfi(XI, YI)   # interpolated values

plt.clf()
plt.imshow(di, extent=(0,1,0,1), origin='lower')
plt.scatter(x,y, color='k')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis((0,1,0,1))
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/rbf.png')