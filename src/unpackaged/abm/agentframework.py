#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:22:06 2018

@author: hannahsherwood
"""
import random

class Agent():
    def __init__(self, environment,agents, neighbourhood):
        self.environment = environment
        self.agents = agents
        self.store = 0 
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        self.neighbours = neighbourhood
    '''
    def hi(self):
        print ("x", self._x)
        print ("y", self._y)
    '''
    
    def move(self):
        # Move the agents.
        if random.random() < 0.5:
            self._x  = (self._x + 1) % 100
        else:
            self._x  = (self._x - 1) % 100
                
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

    def eat(self): 
        if self.environment[self._y][self._x] > 10:
           self.environment[self._y][self._x] -= 10
           self.store += 10
        else:
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
   
    def share_with_neighbours(self, neighbours):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbours:
                sum = self.store + agent.store
                ave = sum/2 
                self.store = ave
                agent.store = ave 
                #print("sharing " + str(dist) + " " + str(ave))

    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
    # Loop through the agents in self.agents .
    # Calculate the distance between self and the current other agent:
    # distance = self.distance_between(agent)
    # distance = self.distance_between(agent)
    
    # If distance is less than or equal to the neighbourhood
        # Sum self.store and agent.store .
        # Divide sum by two to calculate average.
        # self.store = average
            # agent.store = average
    # End if
# End loop

