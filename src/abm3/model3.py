# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:00:03 2023

@author: erica
"""

import random
import matplotlib.pyplot as plt
import time
import math

#set the pseudo-random seed for reproducibility
random.seed(0)

# Create a variable to store the number of agents
#n_agents = 10

#iterations to make the model "move" more than once. 
n_iterations = 1000

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99



      # Calculate the Euclidean distance between (x0, y0) and (x1, y1)#
          # Functions to calculate the distance between each agent#
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
    distance = ((dx * dx) + (dy * dy)) ** 0.5
    return distance
      
   
def get_both_distance():
    """
    Finds the largest maximum distance and lowest minimum between all the agents'
   
    Returns
        minimum and maximum distance between all the agents
    """
    max_distance = 0
    min_distance = math.inf
    for i in range(len(agents)):
         a = agents[i] #reassign a to first variable's position in range calculation
         for j in range(len(agents)):
             b = agents[j]
             #print("i", i, "j", j)
             distance = get_distance(a[0], a[1], b[0], b[1])
             #print("distance between", a, b, distance)
             max_distance = max(max_distance, distance)
             #print("max_distance", max_distance)
             min_distance = min(min_distance, distance)
             #print("min_distance", min_distance)
    return min_distance, max_distance
    #return max_distance

                            #initialize agents#


# Create a loop to run for a range of agents
n_agents_range = range(500, 5000, 500)

# Main Simulation Loop (in n_iterations)

n_agents = 10
agents = []


        # Create a list to store agents - agents are the randomly created x and y variables

for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
            
for ite in range(n_iterations):
    #move the agents
    for i in range(n_agents):
        if random.random() < 0.5:
            agents[i][0] = agents [i][0] +1
        else:
            agents[i][0] = agents [i][0] -1
        #move y
        if random.random() < 0.5:
            agents[i][1] = agents [i][1] +1
        else:
            agents[i][1] = agents [i][1] -1
    print(get_both_distance())
    
# =============================================================================
#             # Apply movement constraints.
#             if agents[i][0] < x_min:
#                 agents[i][0] = x_min
#             if agents[i][1] < y_min:
#                 agents[i][1] = y_min
#             if agents[i][0] > x_max:
#                 agents[i][0] = x_max
#             if agents[i][1] > y_max:
#                 agents[i][1] = y_max
#         #print(agents)
# 
# =============================================================================
