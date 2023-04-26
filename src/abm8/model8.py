

import imageio
import os
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
import operator
import my_modules_8.agentframework as af 
import my_modules_8.io as io
import my_modules_8.geometry as geometry 
import matplotlib.animation as anim
import tkinter as tk

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

def get_max_distance():
    """
    Calculates and returns the largest distance between any two agents.

    Returns
    -------
    max_distance : Number
        The largest distance between any two agents.

    """
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i] #reassign a to first variable's position in range calculation
        for j in range(len(agents)):
            b = agents[j]
            distance = geometry.get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            max_distance = max(distance, max_distance)
    return max_distance

    
        # Define a function that adds up all the values in environment. #
def sum_environment():
    """
    Calculates and returns the sum of all the values in environment

    Returns
    -------
    env_total : Number
        The sum of all agents in the environment.
    """
    env_total = 0
    for row in environment:
        env_total = env_total + sum(row)
    return env_total

def sum_agent_stores():
    """
    Calculates and returns the sum of store variable values 

    Returns
    -------
    sum_agent_stores : Number
        The end sum of all agent stores.
    """
    sum_agent_stores = 0
    for a in agents:
        sum_agent_stores = sum_agent_stores + a.store
    return sum_agent_stores

       
ite = 1
images = []
    
def plot():
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.imshow(environment)
    for i in range(n_agents):
        plt.scatter(agents[i].x, agents[i].y, color='black')
        
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
    
    # For storing images
    global ite
    filename = '../../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    images.append(imageio.imread(filename))
    plt.show()


def update(frames):
    # Model loop
    #for ite in range(1, n_iterations + 1):
    print("Iteration", frames)
    # Move agents
    print("Move and eat")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighborhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
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
 
    # Stopping condition
    global carry_on
    #Average agent stopping condition
    if sum_as / n_agents > 80:
        carry_on = False
        print("stopping condition")
# =============================================================================
#     # Random
#     if random.random() < 0.1:
#         #if sum_as / n_agents > 80:
#         carry_on = False
#         print("stopping condition")
# =============================================================================

    # Plot
    plot()
    
def gen_function():
    global ite
    global carry_on
    while (ite <= n_iterations) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Set the Write data menu to normal.
        menu_0.entryconfig("Write data", state="normal")
        data_written = True
        

def run(canvas):
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    animation.new_frame_seq()
    canvas.draw()

def output():
    # Write data
    print("write data")
    io.write_data('../../data/output/out.txt', environment)
    imageio.mimsave('../../data/output/out.gif', images, fps=3)

def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)
        
                            # Main Simulation Loop #

#initialize agents#
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(agents, i, environment, n_rows, n_cols))
# Animate
# Initialise fig and carry_on
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
data_written = False
    # GUI
root = tk.Tk()
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_0 = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=menu_0)
menu_0.add_command(label="Run model", command=lambda: run(canvas))
menu_0.add_command(label="Write data", command=lambda: output())
menu_0.add_command(label="Exit", command=lambda: exiting())
menu_0.entryconfig("Write data", state="disabled")
    # Exit if the window is closed.
root.protocol('WM_DELETE_WINDOW', exiting)
tk.mainloop()

print (agents, i)
    
    
    
    
    

# =============================================================================
# # Create directory to write images to.
# try:
#     os.makedirs('../../data/output/images/')
# except FileExistsError:
#     print("path exists")
# =============================================================================


    



