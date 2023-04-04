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

# A list to store times
run_times = []

# Create a loop to run for a range of agents
n_agents_range = range(500, 5000, 500)
for n_agents in n_agents_range: 
    
    # Create a list to store agents - agents are the randomly created x and y variables
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    #print(agents)
    
    
   
    # Print the minimum & maximum distance between all the agents from one function

    start = time.perf_counter()
    print("get_both_distance", get_both_distance())
    end = time.perf_counter()
    run_time = end - start
    print("Time taken to calculate distances", run_time)
    run_times.append(run_time)

# =============================================================================
#                            # Plot #
# plt.title("Time taken to calculate maximum distance for different numbers of agent")
# plt.xlabel("Number of agents")
# plt.ylabel("Time")
# j = 0
# for i in n_agents_range:
#     plt.scatter(i, run_times[j], color='black')
#     j = j + 1
# plt.show()
# =============================================================================
