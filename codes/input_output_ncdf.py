# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:53:53 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import the required modules
import numpy as np
from Scientific.IO import NetCDF as nc

## Open the file
#file = nc.NetCDFFile('/home/tomer/my_books/python_in_hydrology/datas/rhum.2003.nc', 'r')
#print(dir(file))
#
#print(file.dimensions)
#
#print(file.variables)
#
#foo = file.variables['rhum']
#rhum = foo.getValue()
#print(foo.typecode())
#
#file.close()

file = nc.NetCDFFile('/home/tomer/my_books/python_in_hydrology/datas/test.nc', 'w')
# Create some global attribute using a constant
setattr(file, 'title', 'trial')
setattr(file, 'description', 'File generated while tesing to write in NetCDF')

## Make some dimensions
#file.createDimension('smallDim', 4)
#file.createDimension('mediumDim', 25)
#file.createDimension('largeDim', 100)
#
## Make a new variable
#varDims = ('smallDim', 'mediumDim')
#var1 = file.createVariable('varOne', 'i', varDims)
#
## Get the size of a variable
#var1Shape = var1.shape
#print "The size of var1 is:", var1Shape

file.createDimension('lat', 73) 
file.createDimension('lon', 144) 
file.createDimension('level', 8) 
file.createDimension('time', 365) 

varDims = 'lat',
lat = file.createVariable('lat', 'f', varDims)
print(file.variables)
lat = np.random.rand(73)

varDims = 'lon',
lon = file.createVariable('lon', 'f', varDims)
lon = np.random.rand(144)

varDims = 'level',
level = file.createVariable('level', 'f', varDims)

varDims = 'time',
time = file.createVariable('time', 'f', varDims)

varDims = 'time', 'level', 'lat', 'lon'
rhum = file.createVariable('rhum', 'f', varDims)

file.close()


file.close()
