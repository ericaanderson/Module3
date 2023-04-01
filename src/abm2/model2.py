# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:13:38 2023

@author: erica
"""

import random
import math
import matplotlib.pyplot as plt
import operator

#set the pseudo-random seed for reproducibility
random.seed(0)

# Create a list to store agents - agents are the x and y variables
agents = []

#the following variable and for loop negates initializing agent variables individually
n_agents = 10
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])

# # Initialise variable x0
# x0 = random.randint(0,99)
# print("x0", x0)

# # Initialise variable y0
# y0 = random.randint(0,99)
# print ("y0", y0)

# agents.append([x0,y0])    #<-- Append x0 & y0 to the list "agents"

# Change x0 (agents[0][0]) and y0 (agents[0][1]) randomly
rn = random.random()
print(rn)

if rn <0.5:  #if the random seed is less than .5, x0 variable in agent spot [0][0] increases by 1
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1
print ("if results for agents[0][0]", agents[0][0])

rn = random.random()
print(rn)
if rn <0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
print ("if results for agents[0][1]", agents[0][1])

# # Initialise variable x1
# x1 = random.randint(0,99)
# print("x1", x1)

# # Initialise variable y1
# y1 = random.randint(0,99)
# print("y1", y1)

# agents.append([x1,y1])    #<-- Append x1 (agents[0][1]) & y1 (agents[1][1]) to the list "agents"

# Change x1 and y1 randomly
rn = random.random()
print(rn)
if rn <0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1
print ("if results for agents[1][0]", agents[1][0])

rn = random.random()
print(rn)
if rn <0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
print ("if results for agents[1][1]", agents[1][1])


# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Set x0 and y0 to equal 0, x1 to equal 3, and y1 to equal 4
x0 = 0
x1 = 0
y0 = 3
y1 = 4

# Calculate the difference in the x coordinates.
dx = x0 - x1
print("dx", dx)
# Calculate the difference in the y coordinates.
dy = y0 - y1
print("dy", dy)

# Square the differences and add the squares
ssd = (dx**2) + (dy**2)
print("ssd", ssd)

# Calculate the square root
distance = ssd ** 0.5
print("distance", distance)

distance = math.sqrt(ssd)
print("distance", distance)


# # Plot the agents
# plt.scatter(agents[0][0], agents[0][1], color='black')
# plt.scatter(agents[1][0], agents[1][1], color='black')
# plt.show()
# # Get the coordinates with the largest x-coordinate
# print(max(agents, key=operator.itemgetter(0)))



for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
maxX = max(agents, key=operator.itemgetter(0))
plt.scatter(maxX[0], maxX[1], color='red')
# Plot the coordinate with the smallest x blue
smX = min(agents, key=operator.itemgetter(0))
plt.scatter(smX[0], smX[1], color='blue')
# Plot the coordinate with the largest y yellow
lrgY = max(agents, key=operator.itemgetter(1))
plt.scatter(lrgY[0], lrgY[1], color='yellow')
# Plot the coordinate with the smallest y green
smY = min(agents, key=operator.itemgetter(1))
plt.scatter(smY[0], smY[1], color='green')
plt.show()