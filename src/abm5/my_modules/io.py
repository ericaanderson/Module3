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

#print ("x_max": + x_max,"y_max:" + y_max)           

print(read_data())
print(n_cols())
print(n_rows()) 
            
            
        #a = ["a"+str(i) for i in range(1, n_cols+1)]

# =============================================================================
#         n_rows = len(list(row))
#         n_cols = len(next(f))
#         #a = ["a"+str(i) for i in range(1, n_cols+1)]
#     x_max = n_cols - 1
#     y_max = n_rows - 1
# =============================================================================
        

    #return('n_rows', n_rows, 'n_cols', n_cols)




# =============================================================================
# def row_coll():
#     f = open('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt', newline='')
#     #n_cols = len(next(f))
#     n_rows = []
#     n_cols = []
#     n_rows.append(len(list(row))  
#     
#     n_cols.append(len(next(f)))     
#     f.close()
# =============================================================================
    

        

# =============================================================================
#     f = open('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt', newline='')
#     
#     n_cols = len(next(f))
#     f.close()
# =============================================================================
    
    
# =============================================================================
#         for value in line:
#             field[c] = row
#             #print(field[c])
#             c = c+1
#         
#         n_rows = len(field[0])
#         n_cols = len(field)
#         #n_rows = len(list(row))
# =============================================================================
        
        #first_line = csv.readline(f, quoting=csv.QUOTE_NONNUMERIC)
        #first_line.count(',') + 1
        
# =============================================================================
#         n_cols = []
#         collumn = list(csv.reader(f, quoting=csv.QUOTE_NONNUMERIC))
#         num_col = len(collumn[0])
#         for value in collumn:
#             n_cols.append(value)
# =============================================================================
        
    
        
# =============================================================================
#         for value in row:
#             number_rows = len(list(row))
#             n_rows.append(number_rows)
# =============================================================================

#    n_rows.append(numberrows)


 
# =============================================================================
#     collumn = []
#     for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#         n_cols = first_line.count(',') + 1

#value in collumn:
#         collumn.append(value)

#   n_cols = len(list(collumn))
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
