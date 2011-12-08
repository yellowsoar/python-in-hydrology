# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:28:50 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from ambhas.copula import Copula

#params = {'axes.labelsize': 17,
#          'text.fontsize': 17,
#          'legend.fontsize': 17,
#          'xtick.labelsize': 17,
#          'ytick.labelsize': 17,
#          'text.usetex': False,
#          'font.size':17}
          
params = {'font.size':10}
plt.rcParams.update(params)


x = np.random.randn(100)
y = 0.2*x+ 2*np.random.rand(100)

# definitions for the axes
rect_scatter = [0.1, 0.1, 0.5, 0.5]
rect_histx = [0.1, 0.65, 0.5, 0.3]
rect_histy = [0.65, 0.1, 0.3, 0.5]

# start with a rectangular Figure
plt.clf()
axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)

# the plots
axScatter.scatter(x, y)
axHistx.hist(x)
axHisty.hist(y, orientation='horizontal')

# set the limit of histogram plots
axHistx.set_xlim( axScatter.get_xlim() )
axHisty.set_ylim( axScatter.get_ylim() )

plt.savefig('/home/tomer/my_books/python_in_hydrology/images/copula_1.png')
plt.close()

params = {'font.size':17}
plt.rcParams.update(params)

foo = Copula(x, y, 'frank')
print(foo.tau)
print(foo.theta)

x1,y1 = foo.generate_xy()

plt.clf()
plt.figure()
plt.scatter(x1,y1, color='g')
plt.scatter(x,y, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/copula_2.png')
plt.close()


# multivariate normal distiburion
mean = [0,5]
cov = [[1,0.4],[0.4,1]] # diagonal covariance, points lie on x or y-axis
data = np.random.multivariate_normal(mean,cov,5000)
print(data.mean(axis=0))
print(np.corrcoef(data.T))
#plt.plot(x,y,'x'); plt.axis('equal'); plt.show()
