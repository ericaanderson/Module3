
import imageio
import os
import random
import matplotlib.pyplot as plt
import math
import operator
import my_modules_6.agentframework as af 
import my_modules_6.io as io
import my_modules_6.geometry as geometry 

environment, n_rows, n_cols = io.read_data()

#set the pseudo-random seed for reproducibility
random.seed(0)

# Create a variable to store the number of agents
n_agents = 10

#iterations to make the model "move" more than once. 
n_iterations = 10

neighborhood = 20

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum an agents x coordinate is allowed to be.
x_max = n_cols - 1
# The maximum an agents y coordinate is allowed to be.
y_max = n_rows - 1



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
            distance = geometry.get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)
            min_distance = min(min_distance, distance)
            #print("min_distance", min_distance)
            return min_distance, max_distance
            #return max_distance

        # Define a function that adds up all the values in environment. #
def sum_environment():
    env_total = sum(environment)
    return env_total
print (sum_environment)
       

def sum_agent_stores():
    sum_agent_stores = sum(agents[i].eat())
    return sum_agent_stores
print (sum_agent_stores)

                            # Main Simulation Loop #

#initialize agents#
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
    print (agents, i)


# Move agents
for i in range(n_agents):
    agents[i].move(x_min, y_min, x_max, y_max)

#Eat Environment
for i in range(n_agents):
    agents[i].eat
    io.write_data
    
    
# Create directory to write images to.
try:
    os.makedirs('../../data/output/images/')
except FileExistsError:
    print("path exists")

# For storing images
global ite
ite = 1
images = []
    
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
# =============================================================================
#     # Print the maximum distance between all the agents
#     print("Maximum distance between all the agents", get_max_distance())
#     # Print the total amount of resource
#     sum_as = sum_agent_stores()
#     print("sum_agent_stores", sum_as)
#     sum_e = sum_environment()
#     print("sum_environment", sum_e)
#     print("total resource", (sum_as + sum_e))
#                  
# =============================================================================

            #print(agents)

    #Limit axis and flip y
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    # Plot 'agents' on the 'environment
    filename = '../../data/output/images/image' + str(ite) + '.png'
    #filename = '../../data/output/images/image' + str(ite) + '.gif'
    plt.savefig(filename)
    plt.show()
    plt.close()
    images.append(imageio.imread(filename))
    #plt.imshow(environment)#
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

    imageio.mimsave('../../data/output/out.gif', images, fps=3)



