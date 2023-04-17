
import random
import matplotlib.pyplot as plt
#import time
#import math
import operator
import my_modules.agentframework as af 
import my_modules.io as io
import my_modules.geometry as geometry

environment = io.read_data()

#set the pseudo-random seed for reproducibility
random.seed(0)

# Create a variable to store the number of agents
n_agents = 10

#iterations to make the model "move" more than once. 
n_iterations = 10

a = af.Agent('i')
#print("type(a)", type(a))

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99




                            #initialize agents#
# =============================================================================
#a = af.Agent()
#print("type(a)", type(a))
# =============================================================================

agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent('i'))
    print (agents, i)


# =============================================================================
# for i in range(n_agents):
#     x_min = min(af.Agent([i].x))
#     y_min = min(af.Agent([i].y))
#     x_max = max(af.Agent([i].x))
#     y_max = max(af.Agent([i].y))
# =============================================================================
 
# Move agents
for i in range(n_agents):
    agents[i].move(x_min, y_min, x_max, y_max)


# Main simulation loop
for ite in range(1, n_iterations + 1):
    print("Iteration", ite)
    # Move agents
    print("Move")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighborhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", get_max_distance())
    # Print the total amount of resource
    sum_as = sum_agent_stores()
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))
                 

            #print(agents)

#Limit axis and flip y
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
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
