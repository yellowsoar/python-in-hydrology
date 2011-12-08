# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:24:40 2011

@author: Sat Kumar Tomer
@website: www.ambhas.com
@email: satkumartomer@gmail.com
"""


fname_input = ['input0', 'input1', 'input2', 'input3']
fname_output = ['output0', 'output1', 'ouput2', 'output3']

for i in range(len(fname_input)):
    
    fname_read = '/home/tomer/my_books/python_in_hydrology/datas/Albedo.prm'
    f_read = open(fname_read, 'r')

    fname_write = '/home/tomer/my_books/python_in_hydrology/datas/Albedo_ii.prm'.replace('ii',str(i))
    f_write = open(fname_write, 'w')
    for line in f_read:
        if 'INPUT_FILENAME' in line:
            line = line.replace('input',fname_input[i])
            print line
        if 'OUTPUT_FILENAME' in line:
            line = line.replace('output',fname_output[i])
            print line
        f_write.write(line)
        
    f_write.close()

f_read.close()
