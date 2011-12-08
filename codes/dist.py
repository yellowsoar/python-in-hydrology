# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:43:16 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# generate instances of normaly distributed random variable
rv1 = st.norm(loc=0, scale=5)
rv2 = st.norm(loc=0, scale=3)
rv3 = st.norm(loc=0, scale=7)

# estimate pdf at some points
x = np.linspace(-50,50, 1000)
y1 = rv1.pdf(x)
y2 = rv2.pdf(x)
y3 = rv3.pdf(x)

# plot the pdf
plt.clf()
plt.plot(x, y1, lw=3, label='scale=5')
plt.plot(x, y2, lw=3, label='scale=3')
plt.plot(x, y3, lw=3, label='scale=7')
plt.xlabel('X', fontsize=20)
plt.ylabel('PDF', fontsize=15)
plt.legend()
plt.savefig('/home/tomer/articles/python/tex/images/norm_pdf.png')

# estimate cdf at some points
y1 = rv1.cdf(x)
y2 = rv2.cdf(x)
y3 = rv3.cdf(x)

# plot the pdf
plt.clf()
plt.plot(x, y1, lw=3, label='scale=5')
plt.plot(x, y2, lw=3, label='scale=3')
plt.plot(x, y3, lw=3, label='scale=7')
plt.xlabel('X', fontsize=20)
plt.ylabel('PDF', fontsize=15)
plt.legend()
plt.savefig('/home/tomer/articles/python/tex/images/norm_cdf.png')


# generate instance cauchy, chi, exponential, uniform
rv1 = st.cauchy(loc=0, scale=5)
rv2 = st.chi(2, loc=0, scale=8)
rv3 = st.expon(loc=0, scale=7)
rv4 = st.uniform(loc=0, scale=20)

# estimate pdf at some points
y1 = rv1.pdf(x)
y2 = rv2.pdf(x)
y3 = rv3.pdf(x)
y4 = rv4.pdf(x)

# plot the pdf
plt.clf()
plt.plot(x, y1, lw=3, label='Cauchy')
plt.plot(x, y2, lw=3, label='Chi')
plt.plot(x, y3, lw=3, label='Exponential')
plt.plot(x, y4, lw=3, label='Uniform')
plt.xlabel('X', fontsize=20)
plt.ylabel('PDF', fontsize=15)
plt.legend()
plt.savefig('/home/tomer/articles/python/tex/images/pdf_all.png')