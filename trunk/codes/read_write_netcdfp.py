# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:28:34 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

from Scientific.IO import NetCDF as nt
import numpy as np

# read the file
fname = '/home/tomer/my_books/python_in_hydrology/datas/rhum.2003.nc'
file = nt.NetCDFFile(fname, 'r')
print(dir(file))

title =file.title
print(title)

dimensions = file.dimensions
print(dimensions)

variables = file.variables
print(variables)

lat = file.variables['lat'].getValue()
lon = file.variables['lon'].getValue()
level = file.variables['level'].getValue()
time = file.variables['time'].getValue()
rhum = file.variables['rhum'].getValue()

print(file.variables['lat'].typecode() )

print(rhum.shape)

file.close()



# write the file
fname = '/home/tomer/my_books/python_in_hydrology/datas/test.nc'
file = nt.NetCDFFile(fname, 'w') 
setattr(file, 'title', title)

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

