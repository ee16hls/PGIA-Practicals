# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
#import sys
import tkinter
# import operator
import matplotlib
matplotlib.use('TkAgg')
matplotlib.use('macosx')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv


"""
Calculate distance between agents
"""

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._y - agents_row_b._y)**2) + 
        ((agents_row_a._x - agents_row_b._x)**2))**0.5
  
"""
Initialise parameters
"""
          
num_of_agents = 10
num_of_iterations = 1000
neighbourhood = 20
agents = []  

## Play with creating agents
#a = agentframework.Agent(environment,agents,neighbourhood)
#print (a)
#print (a.store)
#print (a._x)
#print (a._y)
#
#agents.append(a)
#
#print (agents)
#print (agents[0]._x)

""" 
read in the environment
"""
f = open('in.txt')
reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)

environment = []

for row in f:
    parsed_line = str.split(line, ",")
    rowlist = []
    for value in parsed_line:
        rowlist.append(float(value))
        
    environment.append(rowlist)
f.close()

"""
Make the agents.
"""

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,neighbourhood))
 
  
# print (len(agents))
# for i in range(num_of_agents):
#    agents[i].hi()
    


"""
Move the agents and make them eat and share with neighbours.
"""
    
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
       agents[i].move()
       agents[i].eat()
       #print("store before sharing: " + str(agents[i].store))
       agents[i].share_with_neighbours(neighbourhood)
       #print("store after sharing: " + str(agents[i].store))
       
       

#matplotlib.pyplot.show()
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)


#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

"""
create new agents
"""

agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,neighbourhood))

carry_on = True 

#matplotlib.pyplot.imshow(environment)

def update(frame_number):
    fig.clear()
    global carry_on
    
    
  
    for i in range(num_of_agents):
           agents[i].move()
           agents[i].eat()
           #agents[i].share_with_neighbours()
        
    if random.random() < 0.1:
            carry_on = False 
            print("stopping condition")
    
    # update the environment plot
    matplotlib.pyplot.imshow(environment)
    
    for i in range (num_of_agents):
            matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
            #print(agents[i]._x, agents[i]._y)

def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        yield a 
        a = a + 1 
        
"""
Create the GUI window
"""
root = tkinter.Tk()
root.wm_title("Model")

# animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
# matplotlib.pyplot.show()
    
    
def run():
    global animation 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() #Waits for interactions.


# for a in agents:
    #for b in agents:
        #distance = distance_between(a, b)
        #a.hi()
        #b.hi()
        #print ("distance", distance)

# print (agents[0]._agents[1]._x)

