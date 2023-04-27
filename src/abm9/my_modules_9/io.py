# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:28:40 2023

@author: erica
"""

import csv
#import pandas as pd
import my_modules_9.agentframework as af 


def read_data():
# Read input data
    f = open('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt', newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
        data.append(row)
         
    f.close()
    n_rows = len(data)
    n_cols = len(data[0])
    return (data, n_rows, n_cols)

def write_data(self):
    """
    Write environmental data to a file

    :return:
    """
    file = 'C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/output/environment.txt'
    with open(file, 'wb') as output_file:
        output_file.write(self, af.environment)
        
        
# =============================================================================
# def n_rows():
#     n_rows = []
#     df = pd.read_csv('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt') #===> reads in all the rows, but skips the first one as it is a header.
#     for line in df:
#             rownum = len(df.axes[-1]) #===> Axes of 0 is for a row
#             n_rows.append(rownum)
#     #y_max = n_rows - 1
#     return(n_rows)
#     
#     
# def n_cols():
#     n_cols = []
#     df = pd.read_csv('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt') #===> reads in all the rows, but skips the first one as it is a header.
#     for line in df:
#             colnum=len(df.axes[1]) #===> Axes of 0 is for a row
#             n_cols.append(colnum)
# 
# # =============================================================================
# #     df = pd.read_csv('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt') #===> reads in all the rows, but skips the first one as it is a header.
# # 
# #     n_cols=len(df.axes[1]) #===> Axes of 0 is for a column
# # =============================================================================
#     
#     #x_max = n_cols - 1
#     #return(data) 
#     return(n_cols)
#     n_cols = []
#     df = pd.read_csv('C:/Users/agdtu/work/teaching/2223/GEOG5003/Erica/in.txt') #===> reads in all the rows, but skips the first one as it is a header.
#     for line in df:
#             colnum=len(df.axes[1]) #===> Axes of 0 is for a row
#             n_cols.append(colnum)
#     #x_max = n_cols - 1
#     return(n_cols)
# 
# =============================================================================
#print(read_data())
#print(n_cols())
#print(n_rows()) 