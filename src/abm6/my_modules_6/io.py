# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:28:40 2023

@author: erica
"""

import csv
#import pandas as pd

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
