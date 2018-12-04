# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot
import operator
import random

# Controls number of agents 
num_of_agents = 10

# Makes agent coordinates change an arbituary number of times. 
num_of_iterations = 100 

# Create list of agents with randomised coordinates between 0-100 and remove y0,x0 assignment.
agents = []
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])


# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):    
    
        if random.random() < 0.5:
            agents[i] [0] = (agents[i] [0] + 1) % 100 
        else:
            agents[i] [0] = (agents[i] [0] - 1) % 100 

        if random.random() < 0.5:
            agents[i] [1] = (agents[i] [1] + 1) % 100
        else:
            agents[i] [1] = (agents[i] [1] - 1) % 100

'''
answer = (((agents[0] [0] - agents[1] [0] **2) + ((agents[0] [1] - agents[1] [1]**2))**0.5))
print(answer)
'''

    
#print (agents[i] [0], agents[i] [1])

# Random walk step 2 
#if random.random() < 0.5:
    #agents[0] [0] += 1 
#else:
    #agents[0] [0] -= 1 

#if random.random() < 0.5:
    #agents[0] [1] += 1
#else:
    #agents[0] [1] -+ 0
    
#print (agents[0] [0], agents[0] [1])

# Set up coordinates for agent 2- replaced variable assignment for y1,x1 with agent.
#agents.append([random.randint(0,100), random.randint(0,100)])

# Random walk one step.
if random.random() < 0.5:
    agents[1] [0] += 1 
else:
    agents[1] [0] -= 1 

if random.random() < 0.5:
    agents[1] [1] += 1
else:
    agents[1] [1] -+ 0
    
print (agents[1] [0], agents[1] [1])

# Random walk step 2 
if random.random() < 0.5:
    agents[1] [0] += 1 
else:
    agents[1] [0] -= 1 

if random.random() < 0.5:
    agents [1] [1] += 1
else:
    agents [1] [1] -+ 0
    
print (agents[1] [0], agents[1] [1])


# Calculate the distance between agents with Pythagorus.
#y_diff = (agents[0] [0] - agents[1] [0])
#y_diffsq = y_diff * y_diff 

#x_diff = (agents[0] [1] - agents[1] [1])
#x_diffsq = x_diff * x_diff 

#sum = y_diffsq + x_diffsq
#answer = sum ** 0.5

#print (answer)

print(max(agents, key=operator.itemgetter(1)))
most_east = max(agents, key=operator.itemgetter(1))

# Plot a scatter graph to show agents.
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i] [1], agents[i] [0])
matplotlib.pyplot.show()

#matplotlib.pyplot.scatter(agents[0] [1], agents[0] [0])
#matplotlib.pyplot.scatter(agents[1] [1], agents[1] [0])
# matplotlib.pyplot.scatter(most_east[1], most_east[0], color='red')
#matplotlib.pyplot.show()








 