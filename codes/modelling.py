# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:45:13 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#y_fun = lambda x:x
#y, err = integrate.quad(y_fun,0,10)
#print(y, err)

#y_func = lambda x: np.exp(-x)
#y = integrate.quad(y_func, 0, np.inf)
#print(y)

#f = lambda x,a : np.exp(-a*x)
#y, err = integrate.quad(f, 0, 1, args=(0.5,))


#y1 = lambda x,t : -x*t
#t = np.linspace(0,10)
#y = integrate.odeint(y1, 10, t)
#plt.plot(t,y)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/ode.png')
#plt.close()


## Definition of parameters
#a = 1.
#b = 0.1
#c = 1.5
#d = 0.75
#def dX_dt(X, t=0):
#    """ Return the growth rate of fox and rabbit populations. """
#    return np.array([ a*X[0] -   b*X[0]*X[1] ,
#                  -c*X[1] + d*b*X[0]*X[1] ])
#
#t = np.linspace(0, 15,  1000)              # time
#X0 = np.array([10, 5])                     # initials conditions: 10 rabbits and 5 foxes
#X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
#infodict['message']                     # >>> 'Integration successful.'


params = {'axes.labelsize': 17, 
          'text.fontsize': 17,
          'legend.fontsize': 17,
          'xtick.labelsize': 17,
          'ytick.labelsize': 17,
          'text.usetex': False,
          'font.size':17}

#D = [0.2, 0.1, 0.3]
#A = np.array([[D[0], -D[0], 0],
#             [D[0], -D[0]-D[1], D[1]],
#             [0, D[2], -D[2]]])
#                   
#def dX_dt(sm, t=0):
#    return np.dot(A,sm)
#
#t = np.linspace(0, 10, 100)    
#X0 = np.array([10, 5, 20]) 
#X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
#
#plt.plot(t,X)
#plt.xlabel('Time')
#plt.ylabel('X')
#plt.legend(['X1','X2','X3'])
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/ode_system.png')
#


from scipy import optimize, special
x = np.arange(0,10,0.01)
for k in np.arange(0.5,5.5):
    y = special.jv(k,x)

f = lambda x: -special.jv(k,x)
x_max = optimize.fminbound(f,0,6)

plt.plot(x,y, lw=3)
plt.plot([x_max], [special.jv(k,x_max)],'rs', ms=12)
plt.title('Different Bessel functions and their local maxima')
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/inverse.png')
plt.close()