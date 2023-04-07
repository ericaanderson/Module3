# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 15:00:03 2023

@author: erica
"""

import random
import matplotlib.pyplot as plt
import time
import math
import operator
import agentframework as af

#set the pseudo-random seed for reproducibility
random.seed(0)

# Create a variable to store the number of agents
n_agents = 10

#iterations to make the model "move" more than once. 
n_iterations = 10

a = af.Agent()
print("type(a)", type(a))

# =============================================================================
# # Variables for constraining movement.
# # The minimum x coordinate.
# x_min = 0
# # The minimum y coordinate.
# y_min = 0
# # The maximum x coordinate.
# x_max = 99
# # The maximum y coordinate.
# y_max = 99
# =============================================================================


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
             distance = get_distance(a.x, a.y, b.x, b.y)
             #print("distance between", a, b, distance)
             max_distance = max(max_distance, distance)
             #print("max_distance", max_distance)
             min_distance = min(min_distance, distance)
             #print("min_distance", min_distance)
    return min_distance, max_distance
    #return max_distance

                            #initialize agents#
# =============================================================================
# a = af.Agent()
# print("type(a)", type(a))
# =============================================================================

agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent())
    print(agents[i])
print(agents)

variable = af.Agent()
print(variable)


for ite in range(n_iterations):
    #move the agents
    for i in range(n_agents):
        if random.random() < 0.5:
            agents[i].x = agents [i].x +1
        else:
            agents[i].x = agents [i].x -1
        #move y
        if random.random() < 0.5:
            agents[i].y = agents [i].y +1
        else:
            agents[i].y = agents [i].y -1
    print(get_both_distance())
                  
# =============================================================================
#                    # Apply movement constraints.
#                 if agents[i].x < x_min:
#                     agents[i].x = x_min
#                 if agents[i].y < y_min:
#                     agents[i].y = y_min
#                 if agents[i].x > x_max:
#                     agents[i].x = x_max
#                 if agents[i].y > y_max:
#                     agents[i].y = y_max
#             #print(agents)
# =============================================================================


# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
