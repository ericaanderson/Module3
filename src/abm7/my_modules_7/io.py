# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:28:40 2023

@author: erica
"""

import csv
#import pandas as pd
import my_modules_7.agentframework as af 


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

def write_data(self, environment):
    """
    Write environmental data to a file

    :return:
    """
    file = 'C:/Users/erica/OneDrive/Documents/GitHub/Module3/src/data/output/environment.txt'
    with open(file, 'w') as output_file:
        output_file.write(self)