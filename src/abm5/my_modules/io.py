# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:28:40 2023

@author: erica
"""

import csv

def read_data():
# Read input data
    f = open('C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/input/in.txt', newline='')
    data = []
# =============================================================================
#     field = {}
#     c = 0
# =============================================================================
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
        data.append(row)
        
        n_rows = len(list(row))
        n_cols = len(next(f))
        #a = ["a"+str(i) for i in range(1, n_cols+1)]
        x_max = n_cols - 1
        y_max = n_rows - 1
        
    f.close()
    #return(data)
    return('n_rows', n_rows, 'n_cols', n_cols)

print(read_data())


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
