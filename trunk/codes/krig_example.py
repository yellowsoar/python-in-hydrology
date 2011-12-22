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

# with nugget
x = np.random.rand(100) # uniformly distributed x
y = np.ones(x.shape) 
z = x + 0.2*np.random.randn(len(x))

plt.clf()
plt.plot(x,z, 'ro')
plt.xlabel('x')
plt.ylabel('z')
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_6.png')

foo = krige.OK(x,y,z)
DE, GE = foo.variogram(var_type='averaged', min_lag=0.05)

plt.clf()
plt.plot(DE,GE, 'r--o')
plt.xlabel('lag distance')
plt.ylabel('variogram')
plt.ylim(ymin=0)
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_7.png')

# detrended
z = z-x

plt.clf()
plt.plot(x,z, 'ro')
plt.xlabel('x')
plt.ylabel('z')
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_8.png')

foo = krige.OK(x,y,z)
DE, GE = foo.variogram(var_type='averaged', min_lag=0.05)

plt.clf()
plt.plot(DE,GE, 'r--o')
plt.xlabel('lag distance')
plt.ylabel('variogram')
plt.ylim(ymin=0)
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_9.png')

# two dimensional kriging
x = np.array([6.8, 4.3, 5.9, 11.6, 5.5, 10.8, 8.6, 12.6, 14.7, 13.9, 
     9.47, 14.3, 8.9, 11.9, 11.75])
y = np.array([6.4, 5.0, 6.0, 4.9, 2.7, 8.2, 3.9, 6.7, 10.4, 10.9, 5.6, 
     11.0, 7.3, 6.7, 10.8])
z = np.array([10, 11, 12, 9, 12, 8, 10, 8, 6, 6, 
     10, 6, 8, 8, 6])

foo = krige.OK(x,y,z)
DE, GE = foo.variogram(var_type='averaged', min_lag=0.5)

model_par = {'nugget':0, 'range':20, 'sill':6}

lags = np.linspace(0,6)
G = foo.vario_model(lags, model_par, 'spherical')

plt.clf()
plt.plot(DE,GE, 'rs', ms=10)
plt.plot(lags, G, 'g', lw=3)
plt.xlabel('lag distance')
plt.ylabel('variogram')
plt.ylim(ymin=0)
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_10.png')

Xg, Yg = np.meshgrid(np.linspace(4,16), np.linspace(2,12))
foo.krige(Xg, Yg, model_par, 'spherical')
krig_z = foo.Zg
var_z = foo.s2_k
krig_z.shape = 50,50
var_z.shape = 50,50

plt.clf()
plt.pcolor(Xg, Yg, krig_z)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_11.png')

plt.clf()
plt.pcolor(Xg, Yg, var_z)
plt.plot(x,y, 'ro', ms=12)
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.savefig('/home/tomer/svn/python-in-hydrology/images/krige_12.png')
