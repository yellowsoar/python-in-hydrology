# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:35:03 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

from __future__ import division
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import scikits.timeseries as ts
import scikits.timeseries.lib.plotlib as tpl

params = {'axes.labelsize': 17, 
          'text.fontsize': 17,
          'legend.fontsize': 17,
          'xtick.labelsize': 17,
          'ytick.labelsize': 17,
          'text.usetex': False,
          'font.size':17}

plt.rcParams.update(params)

############################# date axis #########################################
#x = np.arange(500)
#y_sim = np.sin(x/25.0)
#year = [2009, 2010, 2010, 2010, 2011]  
#month = [10, 2, 5, 9, 1]  
#day = [20, 15, 17, 22, 15]  
#y_meas = [0.4, -0.5, 0, 1, 0]
#
#first_date = ts.Date(freq='D',year=2009,month=10,day=05)
#data_series = ts.time_series(y_sim, start_date=first_date)
#
#date = []
#for i in range(len(year)):
#    date.append(datetime.date(year[i], month[i], day[i]))
#meas_series = ts.time_series(y_meas, dates=date,freq='D')
#
#fig = tpl.tsfigure()
#fsp = fig.add_tsplot(111)
#fsp.tsplot(data_series, 'r', lw=3, label='simulated')
#fsp.tsplot(meas_series, 'g*', ms=20, label='measured')
#fsp.set_ylim(-2, 2)
#fsp.grid()
#plt.ylabel('Data')
#fsp.legend(loc='best')
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/date.png')
#plt.close()
#
#
############################# bar chart ######################################### 
#n = 5
#rainfall_mean = 500+300*np.random.rand(n)
#runoff_mean = 0.75*np.random.rand(n)*rainfall_mean
#
#ind = np.arange(n)  # the x locations for the groups
#width = 0.35       # the width of the bars
#
#plt.clf()
#rects1 = plt.bar(ind, rainfall_mean, width, color='g', label='Rainfall')
#rects2 = plt.bar(ind+width, runoff_mean, width, color='m', label='Runoff')
#
#plt.ylabel('Annual sum (mm)')
#plt.title('Water balance')
#plt.xticks(ind+width, ('2001', '2002', '2003', '2004', '2005') )
#
#def autolabel(rects):
#    # attach some text labels
#    for rect in rects:
#        height = rect.get_height()
#        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
#                ha='center', va='bottom')
#
#plt.legend()
#autolabel(rects1)
#autolabel(rects2)
#
#plt.ylim(ymax=1000)
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/bar.png')
#plt.close()
#
#
############################# pie chart #########################################
#rainfall = 1000
#runoff = 0.5*np.random.uniform()*rainfall
#recharge = 0.2*np.random.uniform()*rainfall
#evapotranspiration = rainfall - runoff - recharge
#
# #make a square figure and axes
#plt.figure(figsize=(8,8))
#plt.axis([0.2, 0.2, 0.8, 0.8])
#
#labels = 'Runoff', 'Recharge', 'Evapotranspiration'
#fracs = [runoff, recharge, evapotranspiration]
#
#explode=(0, 0.1, 0)
#plt.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
#plt.title('Annual water balance', bbox={'facecolor':'0.6', 'pad':10})
#
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/pie.png')
#plt.close()
#
############################# imshow #########################################
#band2 = plt.imread('/home/tomer/my_books/python_in_hydrology/datas/band2.tif')
#band3 = plt.imread('/home/tomer/my_books/python_in_hydrology/datas/band3.tif')
#band4 = plt.imread('/home/tomer/my_books/python_in_hydrology/datas/band4.tif')
#
#foo = np.empty((band2.shape[0], band2.shape[1], 3))
#foo[:,:,2] = band2
#foo[:,:,1] = band3
#foo[:,:,0] = band4
#
#plt.clf()
#plt.imshow(foo, interpolation='hanning')
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/imshow.png')
#plt.close()
#
############################# pcolor #########################################
#plt.clf()
#plt.pcolor(band2, cmap=plt.cm.Paired)
#plt.colorbar()
#plt.ylim(ymax=band2.shape[0])
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/pcolor.png')
#plt.close()

############################# colormap #########################################
#a = np.outer(np.arange(0,1,0.01), np.ones(10))
#plt.figure(figsize=(10,5))
#plt.subplots_adjust(top=0.8,bottom=0.05,left=0.01,right=0.99)
#maps=[m for m in plt.cm.datad if not m.endswith("_r")]
#maps.sort()
#l=len(maps)+1
#for i, m in enumerate(maps):
#    plt.subplot(1,l,i+1)
#    plt.axis("off")
#    plt.imshow(a,aspect='auto',cmap=plt.get_cmap(m),origin="lower")
#    plt.title(m,rotation=90,fontsize=10)
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/colormap.png')
#plt.close()

############################## contour #########################################
#from scipy.signal import medfilt2d
#data = medfilt2d(band2, kernel_size=7)
#
#CS = plt.contour(data,10)
#plt.clabel(CS, inline=1, fontsize=10)
#
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/contour.png')
#plt.close()
#
############################## contourf #########################################
#plt.contourf(data,10)
#plt.colorbar()
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/contourf.png')
#plt.close()

############################# 3d plots #########################################
#import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
#
#x = np.random.randn(100)
#y = np.random.randn(100)
#z = np.random.randn(100)
#
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(x, y, z, color='k', marker='s')
#
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/3dscatter.png')
#plt.close()

############################# box plot #########################################
#n = 4
#x = range(n)
#y = 5+np.random.randn(100,4)
#plt.boxplot(y,0,'gD')
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/boxplot.png')
#plt.close()

############################# Q-Q plot #########################################
#import statistics as st
#from scipy.interpolate import interp1d
#
#def Q(data):
#    F, data1 = st.cpdf(data, n=1000)
#    f = interp1d(F, data1)
#    return f(np.linspace(0,1))
#
#x = np.random.randn(1000)
#y = 5*np.random.rand(1000)
#z = np.random.randn(1000)
#
#Qx = Q(x)
#Qy = Q(y)
#Qz = Q(z)
#
#
#plt.clf()
#plt.plot([-5,5] , [-5,5], 'r', lw=1.5, label='1:1 line')
#plt.plot(Qx, Qy, 'gd', label='Uniform')
#plt.plot(Qx, Qz,  'm*', label='Normal')
#plt.axis((-5, 5, -5, 5))
#plt.legend(loc=2)
#plt.xlabel('Normal')
#plt.ylabel('observed')
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/q_q.png')
#plt.close()
############################# multiple y axis  #################################
#fig = plt.figure()
#plt.subplots_adjust(top=0.9,bottom=0.15,left=0.15,right=0.85)
#ax1 = fig.add_subplot(111)
#
#t = np.linspace(0,10)
#y1 = 5*np.sin(t)
#y2 = 10*np.cos(t)
#
#ax1.plot(t, y1, 'g', label='sin')
#ax1.set_xlabel('time (s)')
#
## Make the y-axis label and tick labels match the line color.
#ax1.set_ylabel('sin', color='b')
#for tl in ax1.get_yticklabels():
#    tl.set_color('b')
#ax1.set_ylim(-6,6)
#plt.legend(loc=3)
#
#ax2 = ax1.twinx()
#ax2.plot(t, y2, 'r', label='cos')
#ax2.set_ylabel('cos', color='r')
#for tl in ax2.get_yticklabels():
#    tl.set_color('r')
#ax2.set_ylim(-15,15)    
#
#plt.legend(loc=4)
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/multiple_y.png')
############################# annotations  #################################
#t = np.linspace(0,10)
#y = 5*np.sin(t)
#
#plt.clf()
#plt.plot(t, y, lw=3, color='m')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.annotate('ridge', xy=(np.pi/2, 5),  xycoords='data',
#            xytext=(-20, -75), textcoords='offset points',
#            arrowprops=dict(arrowstyle="->")
#            )
#
#plt.annotate('valley', xy=(1.5*np.pi, -5),  xycoords='data',
#            xytext=(-30, 80), textcoords='offset points',
#            size=20,
#            bbox=dict(boxstyle="round,pad=.5", fc="0.8"),
#            arrowprops=dict(arrowstyle="->",),
#            )
#
#plt.annotate('Annotation', xy=(8, -5),  xycoords='data',
#                xytext=(-20, 0), textcoords='offset points',
#                bbox=dict(boxstyle="round", fc="green"), fontsize=15)
#
#plt.text(3.0, 0, "Down", color = "w", ha="center", va="center", rotation=90,
#            size=15, bbox=dict(boxstyle="larrow,pad=0.3", fc="r", ec="r", lw=2))
#
#plt.text(np.pi*2, 0, "UP", color = "w", ha="center", va="center", rotation=90,
#            size=15, bbox=dict(boxstyle="rarrow,pad=0.3", fc="g", ec="g", lw=2))
#
#
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/annotate.png')

############################# Basemap  #################################
#from mpl_toolkits.basemap import Basemap
#import gdal
#from gdalconst import *
#
## read the data
#dataset = gdal.Open("/home/tomer/my_books/python_in_hydrology/datas/band1.tif",GA_ReadOnly)
#band1 = dataset.GetRasterBand(1).ReadAsArray()
#GT = dataset.GetGeoTransform()
#
#dataset = None
#
## make the co ordinate for the berambadi
#lon = np.linspace(GT[0]+GT[1]/2, GT[0]+GT[1]*(band1.shape[1]-0.5), band1.shape[1])
#lat = np.linspace(GT[3]+GT[5]/2, GT[3]+GT[5]*(band1.shape[0]-0.5), band1.shape[0])
#Lon, Lat = np.meshgrid(lon, lat)
#
## make the base map
#m = Basemap(projection='merc',llcrnrlat=11.72,urcrnrlat=11.825,\
#            llcrnrlon=76.51,urcrnrlon=76.67,lat_ts=20,resolution=None)
#
## draw parallels and meridians.
#m.drawparallels(np.arange(11.7,11.9,.05),labels=[1,0,0,0])
#m.drawmeridians(np.arange(76.4,76.8,.05),labels=[0,0,0,1])
#
## read the shapefile archive
#s = m.readshapefile('/home/tomer/my_books/python_in_hydrology/datas/berambadi','berambadi',
#    color='w',linewidth=2.5)
#
## compute native map projection coordinates of lat/lon grid.
#x, y = m(Lon,Lat)
#
## contour data over the map
#cs = m.pcolor(x,y,band1,cmap=plt.cm.jet)
#cb = plt.colorbar(cs, shrink=0.6, extend='both')
#
#plt.title(" Band 1")
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/basemap.png')
#plt.close()

########################## shared x and y axis ################################
#x1 = range(100)
#x2 = range(125)
#x3 = np.random.rand(100)
#x4 = np.random.rand(100)
#
#y1 = np.random.rand(100)
#y2 = 2.0*np.random.rand(125)
#y3 = np.random.rand(125)
#y4 = 1.5*np.random.rand(100)
#
#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey=True)
#ax1.plot(x1,y1, 'ro')
#ax2.plot(x2,y2, 'go')
#ax3.plot(x2,y3, 'bs')
#ax4.plot(x1,y4, 'mp')
#plt.tight_layout()
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/shared_xy.png')
#plt.show()

######################## sub plots #######################################
x = np.random.rand(25)
y = np.arccos(x)

plt.close('all')
plt.subplot(221)
plt.scatter(x,y)

plt.subplot(223)
plt.scatter(x,y)

plt.subplot(122)
plt.scatter(x,y)

plt.tight_layout()
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/sub_plot1.png')

#plt.close('all')
#fig = plt.figure()
#fig.subplots_adjust(wspace=0.5, hspace=0.4)
#
#ax1 = plt.subplot2grid((3, 3), (0, 0))
#ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
#ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
#ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
#
#ax1.scatter(10*x,y)
#ax2.scatter(10*x,y)
#ax3.scatter(10*x,y)
#ax4.scatter(10*x,y)
#
#plt.savefig('/home/tomer/my_books/python_in_hydrology/images/sub_plot2.png')