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
import my_modules.agentframework as af 
import my_modules.io as io



environment = io.read_data()
n_cols = io.n_cols()
n_rows = io.n_rows()

#set the pseudo-random seed for reproducibility
random.seed(0)

# Create a variable to store the number of agents
n_agents = 10

#iterations to make the model "move" more than once. 
n_iterations = 10



# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum an agents x coordinate is allowed to be.
x_max = int(n_cols - 1)
# The maximum an agents y coordinate is allowed to be.
y_max = int(n_rows - 1)

a = af.Agent('i', 'environment','n_rows','n_cols')
#print("type(a)", type(a))

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
    
    
    
        # Define a function that adds up all the values in environment. #
def env_total():
    env_total = sum(environment)
    return env_total
print (env_total)
       
       
def store_total():
    store = 0
    store = []
    for i in range (n_agents):
        if af.Agent.eat >=10:
           af.Agent.eat -=10
           store.append(store + 10)
        else:
            store.append (store + af.Agent.eat)        
    return (store)
print (store_total())
    #Define a function that adds all the store values in all the agents #



# =============================================================================
# def store_total():
#     store = []
#     for i in range(n_agents):
#         agents[i].eat
#         
#    #store_total = sum (af.Agent(eat))
#     return store_total
# print (store_total())
# =============================================================================



                            #initialize agents#
# =============================================================================
#a = af.Agent()
#print("type(a)", type(a))
# =============================================================================

agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent('i','environment', 'n_rows','n_cols'))
    print (agents, i)
 
# Move agents
for i in range(n_agents):
    agents[i].move(x_min, y_min, x_max, y_max)

#Eat Environment
for i in range(n_agents):
    agents[i].eat


# =============================================================================
# #Limit axis and flip y
# plt.ylim(y_min, y_max)
# plt.xlim(x_min, x_max)
# =============================================================================
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)

# Plot 'agents' on the 'environmen
plt.imshow(environment)
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
