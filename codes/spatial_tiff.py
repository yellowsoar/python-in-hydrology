# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:39:37 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
from __future__ import division
import numpy as np
from osgeo import gdal
from osgeo.gdalconst import *

# generate some synthetic data
X, Y = np.mgrid[0:101, 0:101]
data = np.sin((X**2 + Y**2)/25) 
data_noisy = data + np.random.random(X.shape)
   
# plot the data
plt.matshow(data)
plt.colorbar()
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/spatial_data.png')

plt.matshow(data_noisy)
plt.colorbar(shrink=0.5)
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/spatial_data_noisy.png')

# vector data
vector_x = [10,7,24,16,15,10]
vector_y = [10,23,20,14,7,10]

#plot vector data
plt.clf()
plt.plot(vector_x, vector_y)
plt.axis((5,25,5,25))
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/vect.png')

InPath="/home/tomer/RADARSAT/04Mar10/rawdata/"

# write the raster data (data without noise)
driver = gdal.GetDriverByName('GTiff')
file_name = "/home/tomer/my_books/python_in_hydrology/datas/data.tif"
dataset = driver.Create(file_name, data.shape[1], data.shape[0], 1, gdal.GDT_Float32)
dataset.SetGeoTransform((664000.0, 100.0, 0.0, 1309000.0, 0.0, -100.0))
dataset.GetRasterBand(1).WriteArray(data, 0, 0)
dataset = None

# write the raster data (data with  noise)
driver = gdal.GetDriverByName('GTiff')
file_name = "/home/tomer/my_books/python_in_hydrology/datas/data_noisy.tif"
dataset = driver.Create(file_name, data_noisy.shape[1], data_noisy.shape[0], 1, gdal.GDT_Float32)
dataset.SetGeoTransform((664000.0, 100.0, 0.0, 1309000.0, 0.0, -100.0))
dataset.GetRasterBand(1).WriteArray(data_noisy, 0, 0)
dataset = None

# read the raster data (data with  noise)
driver = gdal.GetDriverByName('GTiff')
file_name = "/home/tomer/my_books/python_in_hydrology/datas/data_noisy.tif"
dataset = gdal.Open(file_name, GA_ReadOnly)
geotransform = dataset.GetGeoTransform()
data = dataset.GetRasterBand(1).ReadAsArray()
dataset = None


