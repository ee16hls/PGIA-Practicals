# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
# import operator
import matplotlib.pyplot
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

matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

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
       
       print("store before sharing: " + str(agents[i].store))
       agents[i].share_with_neighbours(neighbourhood)
       print("store after sharing: " + str(agents[i].store))
 


print("store before sharing: " + str(agents[1].store))
print("store after sharing: " + str(agents[1].store)



matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
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
