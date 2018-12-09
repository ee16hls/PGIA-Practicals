# -*- coding: utf-8 -*-
"""
Programming for Geographical Information Analysis: Core Skills 2018
Model run script- Agent Based Model
@author: Hannah Sherwood
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
import requests
import bs4



  
"""

Initialise parameters

"""
          
num_of_agents = 10
num_of_iterations = 100 
neighbourhood = 20 

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
    parsed_line = str.split(row, ",")
    rowlist = []
    for value in parsed_line:
        rowlist.append(float(value))
    
        
    environment.append(rowlist)
   
f.close()

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

"""
sets the frame size of the plot
"""



#ax.set_autoscale_on(False)


"""
Reads in x and y values from the internet and creates new agents
"""
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs = {"class" : "y"})
td_xs = soup.find_all(attrs = {"class" : "x"})
print (td_ys)
print (td_xs)


# Creating the agents
agents = []

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,agents, neighbourhood, y, x))




fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True 

# matplotlib.pyplot.imshow(environment)

"""
Animation function
"""
def update(frame_number):
    fig.clear()
    global carry_on
    

    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
 
    # update the environment plot
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
       agents[i].move()
       agents[i].eat()
       agents[i].share_with_neighbours(neighbourhood)
    

    for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
        
    
    # stopping conditon
    if random.random() < 0.1:
        carry_on = False 
        print("stopping condition")
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
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
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
