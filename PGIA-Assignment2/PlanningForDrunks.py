#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:05:06 2019

@author: hannahsherwood
"""
"""
Imports
""" 
import matplotlib
import matplotlib.pyplot
matplotlib.use('TkAgg')
matplotlib.use('macosx')
import csv
import agentframework_drunks

"""
Create lists 
"""
environment = []
agents = []
stepped_environment = []
# need a stepped environment list here change this to walked in env?

"""
Define agent parameters 
"""
num_of_agents = 25

"""
Defines the environment frame size in the figure
"""
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

"""
Reads in the environmnet text file 
"""
f = open ("TownPlan.txt")
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

"""
Parses environment data from CSV format into rows
"""
for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
    
# Creating code for the density map output that adds up steps on each coordinate. It uses a 300x300px size, just like the environment used here


for i in range(300):
    rowlist = []
    for j in range(300):
        rowlist.append(0)
    stepped_environment.append(rowlist)
    


# Read into environment data to locate the pub, which is assigned a value of 1


for y, row in enumerate(environment):
    for x, value in enumerate (row):
        if value==1:
            xstartpoint=x
            ystartpoint=y
            


# Assign each agent a house number based on their creation number * 10. Also, append each drunk to the starting position of the pub's coordinates in the environment


for j in range(num_of_agents):
    housenum = (j+1)*10
    agents.append(agentframework_drunks.Agent(environment, agents, housenum, xstartpoint, ystartpoint))
    


# For agents that aren't home, continue moving and store 1 into the stepped_environment file


for i in range (num_of_agents):
    while agents[i].arrived_home==False:
        agents[i].nav()
        stepped_environment[agents[i]._y][agents[i]._x]+=1
        # For agents that made it home, set their arrival status to True to stop the code from rerunning those agents, and tell them to drunkely announce their arrival
        if agents[i].environment[agents[i]._y][agents[i]._x]==agents[i].housenum: # If the agent's location is the same as their house number
            agents[i].arrived_home=True
            print ("What a journey!! WHERE'S MY BED!")
                     


# Create a graph to demonstrate the agents that arrived at their house (all of them by this point due to above code)
	
fig.canvas.set_window_title('Figure of Drunk Agents at their Homes')
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(environment)
for i in range (num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()




# Write the stored values from the stepped_environment list to be able to create a density map


f2= open ('stepped_enviroment_output.csv', 'w', newline= '')
writer = csv.writer (f2, delimiter = ',')
for row in stepped_environment:
    writer.writerow(row)
f2.close

"""

 The following code produces a second figure; the density map of where drunks stepped during the model run

"""


# List creation


stepped_environment_output = []




# Reading in the stepped_environment_output file


f=open ("stepped_enviroment_output.csv")
reader=csv. reader (f, quoting = csv.QUOTE_NONNUMERIC)




# Convering CSV into rows


for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    stepped_environment_output.append(rowlist)




# Creating the size of the figure


fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])




# Creating the density map showing the density of where agents stepped when returning home


fig.canvas.set_window_title('Figure of Density Map')
matplotlib.pyplot.xlim=len(environment)
matplotlib.pyplot.ylim=len(environment)
matplotlib.pyplot.imshow(stepped_environment_output)
matplotlib.pyplot.show()

