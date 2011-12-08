# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:58:04 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# define the variables
h = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
I = np.array([93, 137, 208, 320, 442, 546, 630, 678, 691, 675, 634, 571, 477, 
              390, 329, 247, 184, 134, 108, 90])
C1 = 0.0631
C2 = 0.3442
C3 = 0.5927

Q = np.empty(20) # define the empty array
Q[0] = 85 # initial value of Q

# loop over
for i in range(1,20):
    Q[i] = C1*I[i] + C2*I[i-1] + C3*Q[i-1] 

plt.clf()
plt.plot(I, '-*', label='Inflow')
plt.plot(Q, '--s', label='Outflow')
plt.xlabel('Time', fontsize=20)
plt.ylabel('Flow', fontsize=20)
plt.legend()
plt.savefig('/home/tomer/articles/python/tex/images/muskingum.png')