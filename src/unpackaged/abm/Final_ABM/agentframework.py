#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programming for Geographical Information Analysis: Core Skills 2018
Agent Class 
@author: hannahsherwood
"""

"""
This code creates the agents Class to be used in the agent-based model.
Here the agents have their 'behaviours' defined for them to interact within a
set environment. Behaviours include moving, eating the environment and sharing
their food stores with other agents in a defined radius.
"""

import random

"""
Creates the Agent class
"""

class Agent():
    def __init__(self, environment, agents, neighbourhood, y = None, x = None):
        self.environment = environment
        self.agents = agents
        self.store = 0 
        
        if (x == None) :
            self._x = random.randint(0,300)
        else:
            self._x = x 
        
        if (y == None) :
            self._y = random.randint(0,300)
        else:
            self._y = y
            
        self.neighbours = neighbourhood
    
    #Checking the agents values
    # def hi(self):
        # print ("x", self._x)
        # print ("y", self._y)
    
    
"""
Moves the agents
"""

def move(self):
    # Move x
    if random.random() < 0.5:
        self._x  = (self._x + 1) % 300
    else:
        self._x  = (self._x - 1) % 300
   
    # Move y        
    if random.random() < 0.5:
        self._y = (self._y + 1) % 300
    else:
        self._y = (self._y - 1) % 300


"""
Makes the agents eat 
"""

def eat(self): 
    if self.environment[self._y][self._x] > 10:
       self.environment[self._y][self._x] -= 10
       self.store += 10
    else:
        self.store += self.environment[self._y][self._x]
        self.environment[self._y][self._x] = 0
   
    
"""
Defines Agent stores
"""

def getstore(self):
    return self.store


"""
Makes the agents share food stores with neighbours
"""

def share_with_neighbours(self, neighbourhood):
    for agent in self.agents:
        dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum/2 
            self.store = ave
            agent.store = ave 
            #print("sharing " + str(dist) + " " + str(ave))


"""
Calculates distance between agents 
"""

def distance_between(self, agent):
    return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5


"""
Gives informaion on each agents location and size of store as a string
"""

def __str__(self):
    return ('x =' + str(self._x), 'y =' + str(self._y), 'store =' + str(self.store))