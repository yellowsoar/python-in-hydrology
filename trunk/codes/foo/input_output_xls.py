# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:19:04 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""

import xlrd
import numpy as np

book = xlrd.open_workbook('/home/tomer/my_books/python_in_hydrology/datas/data.xls')
sheet = book.sheet_by_name('Ascending')

sm = np.empty(sheet.nrows-2)
year = np.empty(sheet.nrows-2, int)
month = np.empty(sheet.nrows-2, int)
day = np.empty(sheet.nrows-2, int)
for i in range(sm.shape[0]): 
   sm[i] = sheet.cell_value(i+2,4)  
   year[i] = sheet.cell_value(i+2,0)
   month[i] = sheet.cell_value(i+2,1)
   day[i] = sheet.cell_value(i+2,2)

sm[sm==999.9] = np.nan



# writting output to excel file
import xlwt
book = xlwt.Workbook()
sheet = book.add_sheet('Ascending')
sheet.write(0,0, 'Year')
sheet.write(0,1, 'Month')
sheet.write(0,2, 'Day')
sheet.write(0,3, 'Latitude')
sheet.write(1,3, 'Longitude')

for i in range(len(sm)):
    sheet.write(i+2, 4, sm[i])
    sheet.write(i+2, 0, year[i])
    sheet.write(i+2, 1, month[i])
    sheet.write(i+2, 2, day[i])
    
book.save('/home/tomer/my_books/python_in_hydrology/datas/data1.xls')