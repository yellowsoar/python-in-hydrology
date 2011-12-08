# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:29:09 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# define the variables
theta_e = 0.486
psi = 16.7
K = 0.65
S_e = 0.3
t = 1

#calculate dtheta
dtheta = (1-S_e)*theta_e

# initial guess of F
F_old = K*t
epsilon = 1
F = []
while epsilon > 1e-4:
    F_new = psi*dtheta * np.log(1+F_old/(psi*dtheta)) + K*t
    epsilon = F_new - F_old
    F_old = F_new
    F.append(F_new)


plt.clf()
plt.plot(F,'-ok')
plt.xlabel('Number of iteration',fontsize=25)
plt.ylabel('F',fontsize=20)
plt.savefig('/home/tomer/articles/python/tex/images/F.png')