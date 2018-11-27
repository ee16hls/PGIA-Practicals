#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:19:09 2018

@author: hannahsherwood
"""

import random
# import operator
import matplotlib
matplotlib.use('TkAgg')
matplotlib.use('macosx')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv


f = open('in.txt')
reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)

environment = []

for row in reader:
    
    rowlist = []
    for value in row:
        rowlist.append(value)
        
    environment.append(rowlist)


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._y - agents_row_b._y)**2) + 
        ((agents_row_a._x - agents_row_b._x)**2))**0.5
            
num_of_agents = 10
num_of_iterations = 100 
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


# Make the agents.

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,neighbourhood))
 
"""   
print (len(agents))
for i in range(num_of_agents):
#    agents[i].hi()
    
"""

# Move the agents and make them eat and share with neighbours.
    
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
       agents[i].move()
       agents[i].eat()
       #print("store before sharing: " + str(agents[i].store))
       agents[i].share_with_neighbours(neighbourhood)
       #print("store after sharing: " + str(agents[i].store))
       
       
matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)


for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

# create new agents
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents,neighbourhood))

carry_on = True 

def update(frame_number):
    fig.clear()
    global carry_on
    
    for i in range(num_of_agents):
       agents[i].move()
    
    if random.random() < 0.1:
        carry_on = False 
        print("stopping condition")
   
    for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
        print(agents[i]._x, agents[i]._y)

def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        yield a 
        a = a + 1 
    
# animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()

"""
for a in agents:
    for b in agents:
        distance = distance_between(a, b)
        a.hi()
        b.hi()
        print ("distance", distance)
"""

# print (agents[0]._agents[1]._x)
