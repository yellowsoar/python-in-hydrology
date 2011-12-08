# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:20:06 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import scipy.interpolate

# generate data
x = np.linspace(0,10)
y = 1 + 2*x - 3*x**2 + 15*np.random.randn(50)

# fit the polynomial
z = np.polyfit(x,y,2)

print(z)

# evaluate and plot polynomial 
p = np.poly1d(z)
z_true = np.array([-3, 2, 1])

p_true = np.poly1d(z_true)

plt.clf()
plt.plot(x, y,'.r', label='noisy data')
plt.plot(x, p_true(x), label='True curve')
plt.plot(x, p(x), label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/curve_regre.png')