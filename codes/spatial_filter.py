# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 19:59:24 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import the required library
from osgeo import gdal
from scipy.signal import medfilt2d, wiener
from osgeo.gdalconst import *
import matplotlib.pyplot as plt

# read the raster data 
driver = gdal.GetDriverByName('GTiff')
file_name = "/home/tomer/my_books/python_in_hydrology/datas/data_noisy.tif"
dataset = gdal.Open(file_name, GA_ReadOnly)
geotransform = dataset.GetGeoTransform()
data = dataset.GetRasterBand(1).ReadAsArray()
dataset = None

# median filter of 7X7 window
data_median = medfilt2d(data, kernel_size=3)

# filter the image using wiener filter of window (7X7)
data_wiener = wiener(data, mysize=(3,3), noise=None)

# plot the data
plt.clf()
plt.matshow(data_median)
plt.colorbar()
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/median.png')

plt.clf()
plt.matshow(data_wiener)
plt.colorbar()
plt.savefig('/home/tomer/my_books/python_in_hydrology/images/wiener.png')

# save the data into tif format
driver = gdal.GetDriverByName('GTiff')
file_name = "/home/tomer/my_books/python_in_hydrology/datas/data_filtered.tif"
dataset = driver.Create(file_name, data_wiener.shape[1], data_wiener.shape[0], 1, gdal.GDT_Float32)
dataset.SetGeoTransform(geotransform)
dataset.GetRasterBand(1).WriteArray(data_wiener, 0, 0)
dataset = None

