# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:21:32 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# genearte some sythetic data
x = np.random.randn(100)

# compute histogram
n, low_range, binsize, extrapoints = st.histogram(x)
upper_range  = low_range+binsize*len(n)
bins = np.linspace(low_range, upper_range, len(n)+1)
#bins = 0.5*(bins[:-1] + bins[1:])

# plot the histogram
plt.clf()
plt.bar(bins[:-1], n, width=0.4, color='red')
plt.xlabel('X', fontsize=20)
plt.ylabel('number of data points in the bin', fontsize=15)
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/hist.png')

# compute and plot the relfreq
relfreqs, lowlim, binsize, extrapoints = st.relfreq(x)
plt.clf()
plt.bar(bins[:-1], relfreqs, width=0.4, color='magenta')
plt.xlabel('X', fontsize=20)
plt.ylabel('Relative frequencies', fontsize=15)
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/relfreq.png')

# compute and plot pdf
plt.clf()
n, bins, patches = plt.hist(x, 10, normed=1, facecolor='yellow', alpha=0.5)
plt.xlabel('X', fontsize=15)
plt.ylabel('PDF', fontsize=15)
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/pdf.png')

# compute and plot cdf
cumfreqs, lowlim, binsize, extrapoints = st.cumfreq(x)
plt.clf()
plt.bar(bins[:-1], cumfreqs/cumfreqs[-1], width=0.4, color='black', alpha=0.45)
plt.xlabel('X', fontsize=15)
plt.ylabel('CDF', fontsize=15)
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/cdf.png')

