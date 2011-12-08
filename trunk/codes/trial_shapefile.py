# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 18:42:32 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
import shapefile
import numpy as np

# data
x = [10, 7, 24, 16, 15, 10]
y = [10, 23, 20, 14, 7, 10]
z = [0, 0, 0, 0, 0, 0]
data = np.random.rand(6)

# create point shapefile
w = shapefile.Writer(shapefile.POINT)

# add points
for i in range(len(x)):
    w.point(x[i], y[i], z[i], data[i]) 

w.field('FIRST_FLD')
w.field('SECOND_FLD')
w.record('First','Point')
w.record('Second','Point')
w.record('Third','Point')
w.record('Fourth','Point')
w.record('Fifht','Point')
w.record('Sixth','Point')
w.save('/home/tomer/my_books/python_in_hydrology/datas/points.shp')

# create polygon shapefile
w = shapefile.Writer(shapefile.POLYLINE)

# add polyline
w = shapefile.Writer(shapefile.POLYLINE)
w.poly(parts=[[[x[0],y[0]], 
               [x[1],y[1]],
               [x[2],y[2]],
               [x[3],y[3]],
               [x[4],y[4]],
               [x[5],y[5]]]], shapeType=shapefile.POLYLINE)

w.field('FIRST_FLD')
w.field('SECOND_FLD')
w.record('First','Line')
w.save('/home/tomer/my_books/python_in_hydrology/datas/poly.shp')

# read the points shapefile
sf = shapefile.Reader('/home/tomer/my_books/python_in_hydrology/datas/points.shp')
shapes = sf.shapes()

# Read the second point
print(shapes[1].points)



