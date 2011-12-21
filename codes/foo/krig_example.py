# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:23:29 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required library
from ambhas import krige
import numpy as np
import matplotlib.pyplot as plt

params = {'axes.labelsize': 17, 
          'text.fontsize': 17,
          'legend.fontsize': 17,
          'xtick.labelsize': 17,
          'ytick.labelsize': 17,
          'text.usetex': False}
plt.rcParams.update(params)

x = np.random.rand(100) # uniformly distributed x
y = np.ones(x.shape) 
z = np.cos(2*x/0.001) 

plt.clf()
plt.plot(x,z, 'ro')
plt.xlabel('x')
plt.ylabel('z')
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_1.png')

foo = krige.OK(x,y,z)
D,G = foo.variogram(var_type='scattered')

plt.clf()
plt.plot(D,G, '.')
plt.xlabel('lag distance')
plt.ylabel('variogram')
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_2.png')

DE,GE = foo.variogram(var_type='averaged', min_lag=0.025)

plt.clf()
plt.plot(DE,GE, 'r--o')
plt.xlabel('lag distance')
plt.ylabel('variogram')
plt.ylim((0,2))
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_3.png')

z = np.cos(2*x/0.25) 

plt.clf()
plt.plot(x,z, 'ro')
plt.xlabel('x')
plt.ylabel('z')
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_4.png')

foo = krige.OK(x,y,z)
DE,GE = foo.variogram(var_type='averaged', min_lag=0.025)

plt.clf()
plt.plot(DE,GE, 'r--o')
plt.xlabel('lag distance')
plt.ylabel('variogram')
plt.ylim((0,2))
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_5.png')

foo = krige.OK(x,y,z)
D,G = foo.variogram(var_type='scattered')

x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)
foo = krige.OK(x,y,z)
DE, GE = foo.variogram(var_type='averaged', min_lag=0.025)



