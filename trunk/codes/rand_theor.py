# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:24:48 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# NORMAL DISTRIBUION
rv = st.norm(loc=0, scale=5)

x1 = np.linspace(-20, 20, 1000)
y1 = rv.pdf(x1)

# compute and plot pdf
plt.clf()
fig = plt.figure()
fig.subplots_adjust(wspace=0.4)

plt.subplot(2,2,1)
x = rv.rvs(size=100)
n, bins, patches = plt.hist(x, 20, normed=1, facecolor='yellow', alpha=0.5)
plt.plot(x1, y1, 'r', lw=3)
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.axis([-20, 20, 0, 0.10])
plt.text(-18,0.08,'n=100')

plt.subplot(2,2,2)
x = rv.rvs(size=1000)
n, bins, patches = plt.hist(x, 20, normed=1, facecolor='green', alpha=0.5)
plt.plot(x1, y1, 'r', lw=3)
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.axis([-20, 20, 0, 0.10])
plt.text(-18,0.08,'n=1000')

plt.subplot(2,2,3)
x = rv.rvs(size=10000)
n, bins, patches = plt.hist(x, 20, normed=1, facecolor='black', alpha=0.5)
plt.plot(x1, y1, 'r', lw=3)
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.axis([-20, 20, 0, 0.10])
plt.text(-18,0.08,'n=10000')

plt.subplot(2,2,4)
x = rv.rvs(size=100000)
n, bins, patches = plt.hist(x, 20, normed=1, facecolor='magenta', alpha=0.5)
plt.plot(x1, y1, 'r', lw=3)
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.axis([-20, 20, 0, 0.10])
plt.text(-18,0.08,'n=100000')

plt.savefig('/home/tomer/my_books/python_in_hydrology/images/rand_theo.png')

# LAPLACE DISTRIBUION
rv = st.laplace(loc=0, scale=15)

x1 = np.linspace(-100, 100, 1000)
y1 = rv.pdf(x1)

# compute and plot pdf
plt.clf()
fig = plt.figure()
fig.subplots_adjust(wspace=0.4)

plt.subplot(2,2,1)
x = rv.rvs(size=100)
n, bins, patches = plt.hist(x, 20, normed=1, facecolor='yellow', alpha=0.5)
plt.plot(x1, y1, 'r', lw=3, label='scale=5')
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.ylim(ymax=0.04)
plt.xlim((-100,100))
plt.text(-80,0.035,'n=100')

plt.subplot(2,2,2)
x = rv.rvs(size=1000)
n, bins, patches = plt.hist(x, 20, normed=1, facecolor='green', alpha=0.5)
plt.plot(x1, y1, 'r', lw=3, label='scale=5')
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.ylim(ymax=0.04)
plt.xlim((-100,100))
plt.text(-80,0.035,'n=1000')

plt.subplot(2,2,3)
x = rv.rvs(size=10000)
n, bins, patches = plt.hist(x, 20, normed=1, facecolor='black', alpha=0.5)
plt.plot(x1, y1, 'r', lw=3, label='scale=5')
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.ylim(ymax=0.04)
plt.xlim((-100,100))
plt.text(-80,0.035,'n=10000')

plt.subplot(2,2,4)
x = rv.rvs(size=100000)
n, bins, patches = plt.hist(x, 20, normed=1, facecolor='magenta', alpha=0.5)
plt.plot(x1, y1, 'r', lw=3, label='scale=5')
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.ylim(ymax=0.04)
plt.xlim((-100,100))
plt.text(-80,0.035,'n=100000')

plt.savefig('/home/tomer/my_books/python_in_hydrology/images/laplace_rand.png')