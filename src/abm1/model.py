# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:13:38 2023

@author: erica
"""

import random
import math
#set the pseudo-random seed for reproducibility
#random.seed(8)


# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0
print ("y0", y0)

# Change x0 and y0 randomly
rn = random.random()
print(rn)

if rn <0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print ("if results for x0", x0)

if rn <0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    print ("if results for y0", y0)

# Initialise variable x1
x1 = 3
print("x1", x1)

# Initialise variable y1
y1 = 4
print("y1", y1)



# # Change x1 and y1 randomly
if rn <0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print ("if results for x1", x1)

if rn <0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print ("if results for y1", y1)

# =============================================================================
# maybe could also do it this way? depends on how "random" you want it...
# x1 = random.random()
# print("x1", x1)
# y1 = random.random()
# print("y1", y1)
# =============================================================================


# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Calculate the difference in the x coordinates.
xE = x0 - x1
print("xE", xE)
# Calculate the difference in the y coordinates.
yE = y0 - y1
print("yE", yE)

# Square the differences 
xEs = xE**2
print("xEs", xEs)

yEs = yE**2
print("yEs", yEs)

#add the squares
sumsqr = xEs + yEs
print ("sumsqr", sumsqr)

# Calculate the square root
sqrroot = sumsqr ** 0.5
print("sqrroot", sqrroot)

# =============================================================================
# alternative way to calculate square root
# sqrroot2 = math.sqrt(sumsqr)
# print("sqrroot2", sqrroot2)
# 
# =============================================================================
