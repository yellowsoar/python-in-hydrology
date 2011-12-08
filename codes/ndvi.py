# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:51:12 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import the required library
from __future__ import division
from osgeo import gdal
from osgeo.gdalconst import *
import matplotlib.pyplot as plt

# read the raster data 
driver = gdal.GetDriverByName('GTiff')
file_name = "/home/tomer/my_books/python_in_hydrology/datas/band3.tif"
dataset = gdal.Open(file_name, GA_ReadOnly)
geotransform = dataset.GetGeoTransform()
projection = dataset.GetProjection()
band3 = dataset.GetRasterBand(1).ReadAsArray()
dataset = None
print(geotransform)
print(projection)

file_name = "/home/tomer/my_books/python_in_hydrology/datas/band4.tif"
dataset = gdal.Open(file_name, GA_ReadOnly)
band4 = dataset.GetRasterBand(1).ReadAsArray()
dataset = None

# check the data type
print(band3.dtype)

# compute ndv
ndvi = (band4-band3)/(band4+band3)

plt.matshow(ndvi,cmap=plt.cm.jet, vmin=-1, vmax=1)
plt.colorbar(shrink=0.8)
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/ndvi.png')
plt.close()
