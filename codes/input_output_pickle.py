# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:31:47 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

import cPickle as pickle

var = [2, 5, 8, 'foo']

pickle.dump(var, open( "/home/tomer/my_books/python_in_hydrology.pkl", "wb" ) )

var1 = pickle.load( open( "/home/tomer/my_books/python_in_hydrology.pkl", "rb" ) )
print(var1)