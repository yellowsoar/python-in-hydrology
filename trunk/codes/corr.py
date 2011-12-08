# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:02:22 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

x = np.linspace(0,10)
y1 = 2*x 
y2 = y1 + 2*np.random.randn(50)
y3 = x**2
y4 = y3 + 2*np.random.randn(50)
y5 = (x-5)**2
y6 = y5 + 2*np.random.randn(50)

plt.clf()
plt.subplot(2,3,1)
plt.plot(x, y1, '.')
plt.text(2,15,'(a)')

plt.subplot(2,3,2)
plt.plot(x, y2, '.')
plt.text(2,15,'(b)')

plt.subplot(2,3,3)
plt.plot(x, y3, '.')
plt.text(2,80,'(c)')

plt.subplot(2,3,4)
plt.plot(x, y4, '.')
plt.text(2,100,'(d)')

plt.subplot(2,3,5)
plt.plot(x, y5, '.')
plt.text(2,20,'(e)')

plt.subplot(2,3,6)
plt.plot(x, y6, '.')
plt.text(2,25,'(f)')
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/corr.png')

# calculate r 
r1, p1 = st.pearsonr(x,y1)
r2, p2 = st.pearsonr(x,y2)
r3, p3 = st.pearsonr(x,y3)
r4, p4 = st.pearsonr(x,y4)
r5, p5 = st.pearsonr(x,y5)
r6, p6 = st.pearsonr(x,y6)

# print r's
print('%1.2f %1.2f %1.2f %1.2f %1.2f %1.2f')%(r1,r2,r3,r4,r5,r6)

# calculate rho
rho1, p1 = st.spearmanr(x,y1)
rho2, p2 = st.spearmanr(x,y2)
rho3, p3 = st.spearmanr(x,y3)
rho4, p4 = st.spearmanr(x,y4)
rho5, p5 = st.spearmanr(x,y5)
rho6, p6 = st.spearmanr(x,y6)

# print rho's
print('%1.2f %1.2f %1.2f %1.2f %1.2f %1.2f')%(rho1,rho2,rho3,rho4,rho5,rho6)

# estiamte kendall's tau
tau1, p1 = st.kendalltau(x,y1)
tau2, p2 = st.kendalltau(x,y2)
tau3, p3 = st.kendalltau(x,y3)
tau4, p4 = st.kendalltau(x,y4)
tau5, p5 = st.kendalltau(x,y5)
tau6, p6 = st.kendalltau(x,y6)

# print tau's
print('%1.2f %1.2f %1.2f %1.2f %1.2f %1.2f')%(tau1,tau2,tau3,tau4,tau5,tau6)

#print st.linregress(x,y)