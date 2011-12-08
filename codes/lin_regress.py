# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:19:14 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# generate the data
n = 100 # length of the data
x = np.random.rand(n)
y = 3 + 7*x + np.random.randn(n)

# perform linear regression
b, a, r, p, e = st.linregress(x, y)

# error of fitting and measured data
eps = y - a - b*x
     
# x axis to plot the PI
x1 = np.linspace(0, 1)

# variace of fitting error
e_pi = np.var(eps)*(1+1.0/n + (x1-x.mean())**2/np.sum((x-x.mean())**2))

# z value using the t distribution and with dof = n-2
z = st.t.ppf(0.95, n-2)

# prediction interval
pi = np.sqrt(e_pi)*z

zl = st.t.ppf(0.10, n-2)
zu = st.t.ppf(0.90, n-2)
ll = a + b*x1 + np.sqrt(e_pi)*zl
ul = a + b*x1 + np.sqrt(e_pi)*zu

# plot
plt.clf()
plt.plot(x1,3+7*x1, 'r', lw=3, label='True line')
plt.plot(x,y,'ro', label='measured')
plt.plot(x1,a+b*x1, 'k', lw=3, label='Fitted line')
plt.plot(x1,ll,'--', label='10%')
plt.plot(x1,ul,'--', label='90%')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/lin_regress.png')