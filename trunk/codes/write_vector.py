# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:45:56 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

# import required modules
import ogr

lat = [29.4,28.6,13.0,11.8]
lon = [78.1,77.2,77.8,76.6]
name = ['Bijnor', 'Delhi', 'Bangalore', 'Berambadi']

driver = ogr.GetDriverByName("ESRI Shapefile")
ds = driver.CreateDataSource('/home/tomer/my_books/python_in_hydrology/datas/')
layer = ds.CreateLayer('location', geom_type=ogr.wkbPoint)
field_defn = ogr.FieldDefn('Name', ogr.OFTString )
field_defn.SetWidth(16)

layer.CreateField(field_defn)




i = 0
for i in range(len(name)):
    feature_defn = layer.GetLayerDefn()
    feature = ogr.Feature(feature_defn)
    feature.SetField('Name', name[i])
    pt = ogr.Geometry(ogr.wkbPoint)
    pt.SetPoint_2D(0, lon[i], lat[i])
    feature.SetGeometry(pt)
    layer.CreateFeature(feature)
    feature.Destroy()
ds.Destroy()