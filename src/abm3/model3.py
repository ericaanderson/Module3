# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:00:03 2023

@author: erica
"""

import random
import math
import matplotlib.pyplot as plt
import operator

#set the pseudo-random seed for reproducibility
random.seed(0)

# Create a variable to store the number of agents
n_agents = 10

                            #initialize agents#

# Create a list to store agents - agents are the x and y variables
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

      # Calculate the Euclidean distance between (x0, y0) and (x1, y1)#
# Create the function get_distance and return distance calculated

    # Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
 
def get_distance(x0, y0, x1, y1):
    """
    Calculates difference between input x0,y0 and x1,y1 coordinates
    
    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair
    y0 : Number
        The y-coordinate of the first coordinate pair
    x1 : Number
        The x-coordinate of the second coordinate pair
    y1 : Number
        The y-coordinate of the second coordinate pair

    Returns:
        Euclidean distance between coordinates (x0, y0) and (x1,y1)
    """

    # Calculate the difference in the x coordinates.
    dx = x0 - x1
    # Calculate the difference in the y coordinates.
    dy = y0 - y1
    # Square the differences, add the squares, calculate square root
    return ((dx * dx) + (dy * dy)) ** 0.5
    print(get_distance(x0, y0, x1, y1))


max_distance = 0 # Initialise max_distance
for a in agents:
    for b in agents:
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)
        
def get_max_distance():
    """
    Finds the largest maximum distance between all the agents' max distance
    "d" assigns a signle value to the agents' max distance. 
   
    Returns
        maximum distance between all the agents
    """
    for d in max_distance:
        get_max_distance = max(max_distance)
        print("get_max_distance", get_max_distance)


# =============================================================================
#                            # Plot #
# for i in range(n_agents):
#     plt.scatter(agents[i][0], agents[i][1], color='black')
# # Plot the coordinate with the largest x red
# lx = max(agents, key=operator.itemgetter(0))
# plt.scatter(lx[0], lx[1], color='red')
# # Plot the coordinate with the smallest x blue
# sx = min(agents, key=operator.itemgetter(0))
# plt.scatter(sx[0], sx[1], color='blue')
# # Plot the coordinate with the largest y yellow
# ly = max(agents, key=operator.itemgetter(1))
# plt.scatter(ly[0], ly[1], color='yellow')
# # Plot the coordinate with the smallest y green
# sy = min(agents, key=operator.itemgetter(1))
# plt.scatter(sy[0], sy[1], color='green')
# plt.show()
# =============================================================================
