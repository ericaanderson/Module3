# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:28:40 2023

@author: erica
"""

import csv
import pandas as pd

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
    return(data)


def n_rows():
    df = pd.read_csv('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt') #===> reads in all the rows, but skips the first one as it is a header.

    n_rows=len(df.axes[-1]) #===> Axes of 0 is for a row
    
    y_max = n_rows - 1
    return(n_rows)
       
def n_cols():
    df = pd.read_csv('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt') #===> reads in all the rows, but skips the first one as it is a header.

    n_cols=len(df.axes[1]) #===> Axes of 0 is for a column
    
    x_max = n_cols - 1
    #return(data) 
    return(n_cols)



#Write a function to write out the values of environment to a file 
# call this function after the main module

def write_data(self):
    """
    Write environmental data to a file

    :return:
    """
    file = 'C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/output/environment.txt'
    with open(file, 'wb') as output_file:
        output_file.write(self)






# =============================================================================
# def area():
#     df = pd.read_csv('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt') #===> reads in all the rows, but skips the first one as it is a header.
#     
#     n_rows=len(df.axes[-1]) #===> Axes of 0 is for a row
#     n_cols=len(df.axes[1]) #===> Axes of 0 is for a column
#     x_max = n_cols - 1
#     y_max = n_rows - 1
#     return("Number of Rows: "+str(n_rows), "Number of Columns: "+str(n_cols))
# =============================================================================


# =============================================================================
# 
# Change the 'read_data' function so it checks that each row of 'data' contains
# the same number of values. Also change the function so it returns the number
# of lines (n_rows) and the number of values in each line (n_cols) as well as 'data'. 
# (Hint, pack these in a tuple, and unpack the returned tuple in the code that 
# calls the function initialising variables 'n_rows' and 'n_cols' as well as 
# 'environment'.)
# =============================================================================
