# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:04:06 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# generate the synthetic data
Rn = 150+100*np.random.rand(100) # lower bound = 150, upper boun = 250
T = 25+3*np.random.randn(100) # mean = 25, std = 3
Rh = 0.2+0.6*np.random.rand(100) # lower bound = 0.2, upper boun = 0.8
u2 = 3+np.random.randn(100) # mean = 3, std = 1

# define constants
rho_w = 997
rho_a = 1.19
p = 101.1e3
z2 = 2
z0 = 0.03e-2
k = 0.4
Cp = 1005

# calculate using energy balance method
lv = (2500-2.36*T)*1000 # multiplied by thousand to convert from KJ/kg to J/kg
Er = 200/(lv*997)
Er *= 1000*86400 # convert from m/s to mm/day

# calculate using aerodynamic method
B = 0.622*k**2*rho_a*u2/(p*rho_w*(np.log(z2/z0))**2)
e_s = 611*np.exp(17.27*T/(237.3+T))
e_a = Rh*e_s
Ea = B*(e_s-e_a)
Ea *= 1000*86400 # convert from m/s to mm/day

# combined method
gamma = Cp*p/(0.622*lv) # since kh/kw = 1, hence they are dropped form eq.
delta = 4098*e_s/(237.3+T)**2
w = delta/(delta+gamma)
E = w*Er + (1-w)*Ea

# plot the results
plt.clf()
plt.subplot(2,2,1)
plt.plot(Er)
plt.xlabel('Time')
plt.ylabel('Er')

plt.subplot(2,2,2)
plt.plot(Ea)
plt.xlabel('Time')
plt.ylabel('Ea')

plt.subplot(2,2,3, axisbg='y')
plt.plot(E)
plt.xlabel('Time')
plt.ylabel('E')

plt.subplot(2,2,4, axisbg='g')
plt.plot(w)
plt.xlabel('Time')
plt.ylabel('Er/E')
plt.savefig('/home/tomer/articles/python/tex/images/E.png')


# plot the results
fig = plt.figure()
fig.subplots_adjust(wspace=0.6)
plt.subplot(2,2,1)
plt.plot(Er)
plt.xlabel('Time')
plt.ylabel('Er')

plt.subplot(2,2,2)
plt.plot(Ea)
plt.xlabel('Time')
plt.ylabel('Ea')

plt.subplot(2,2,3, axisbg='y')
plt.plot(E)
plt.xlabel('Time')
plt.ylabel('E')

plt.subplot(2,2,4, axisbg='g')
plt.plot(w)
plt.xlabel('Time')
plt.ylabel('Er/E')
plt.savefig('/home/tomer/articles/python/tex/images/corr_E.png')