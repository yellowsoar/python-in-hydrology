# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 16:42:35 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

import ogr

ds = ogr.Open( '/home/tomer/my_books/python_in_hydrology/datas/' )
lyr = ds.GetLayerByName('location' )
#lyr.ResetReading()

print("\n")
print("{} \t {:10s} \t {} \t {}".format('SI', 'Name', 'Latitude', 'Longitude'))
for feat in lyr:
    geom = feat.GetGeometryRef()
    print('{0} \t {1:10s} \t {2:.3f} \t \t {3:.3f}'.format(0, feat.GetFieldAsString(0), geom.GetX(), geom.GetY()))
   
ds = None