# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:58:26 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

#genrate locations and rainfall
x = np.random.rand(10)
y = np.random.rand(10)
rain = 10*np.random.rand(10)

#plot the locations
plt.clf()
plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim((0,1))
plt.ylim((0,1))
plt.savefig('/home/tomer/articles/python/tex/images/loc.png')

#generate the desired grid, where rainfall is to be interpolated
X,Y = np.meshgrid(np.linspace(0,1,1000), np.linspace(0,1,1000))

#perform the gridding
grid_rain = griddata((x,y), rain, (X, Y))

#plot the contour
plt.clf()
plt.contourf(X,Y,grid_rain)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(x, y, s=30, c='r')
plt.xlim((0,1))
plt.ylim((0,1))
plt.savefig('/home/tomer/articles/python/tex/images/grid_rain.png')
