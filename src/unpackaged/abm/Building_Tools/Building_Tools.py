#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:10:27 2018

@author: hannahsherwood
"""
import random
import operator
import matplotlib.pyplot
import time 

time_list = []
magnitude_list = []
for p in range(4, 7):
    

    start = time.clock()
    
    def distance_between(agents_row_a, agents_row_b):
        return(((agents_row_a[0]- agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    
    num_of_agents = 5**p
    
    magnitude_list.append(num_of_agents)
    
    num_of_iterations = 100
    agents = []
    
    # Make the agents.
    for i in range(num_of_agents):
        agents.append([random.randint(0,99),random.randint(0,99)])
    
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
    
            if random.random() < 0.5:
                agents[i][0] = (agents[i][0] + 1) % 100
            else:
                agents[i][0] = (agents[i][0] - 1) % 100
    
            if random.random() < 0.5:
                agents[i][1] = (agents[i][1] + 1) % 100
            else:
                agents[i][1] = (agents[i][1] - 1) % 100
    
    
    # Pythagorus code: answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5 print(answer)
    
    # Plot the agents on a graph
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    matplotlib.pyplot.show()
    
    # Calculate the distance between agents 
    distance = distance_between(agents[0], agents[1])
    print(distance)
    
    # Repeat and calculate the distance between all agents without repeating pairs or testing agents against themselves 
    dist_list = []
    for i in range(num_of_agents):
        for j in range(num_of_agents):
            if (i<j):
                distance= distance_between(agents[i], agents[j])
                print ("distance_between", agents[i], "and" , agents[j])
                print (distance)
                dist_list.append(distance)
                
    print(dist_list)
    
    max_dist = max(dist_list)
    min_dist = min(dist_list)
    
    
    # Find max and min distances between agents 
                
    
    
    # Print the time it took to run the whole code            
    end = time.clock()
    print("time = " + str(end - start))
    
    time_list.append(end - start)
    
    
    
matplotlib.pyplot.plot(time_list, magnitude_list)

matplotlib.pyplot.show()