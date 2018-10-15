# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

# Set up variables with random starting value between 0-100.
y0 = random.randint(0,100)
x0 = random.randint(0,100)

# Random walk one step.
if random.random() < 0.5:
    y0 += 1 
else:
    y0 -= 1 

if random.random() < 0.5:
    x0 += 1
else:
    x0 -+ 0
    
print (y0, x0)

# Random walk step 2 
if random.random() < 0.5:
    y0 += 1 
else:
    y0 -= 1 

if random.random() < 0.5:
    x0 += 1
else:
    x0 -+ 0
    
print (y0, x0)

# Set up variables with  random starting value between 0-100.
y1 = random.randint(0,100)
x1 = random.randint(0,100)

# Random walk one step.
if random.random() < 0.5:
    y1 += 1 
else:
    y1 -= 1 

if random.random() < 0.5:
    x1 += 1
else:
    x1 -+ 0
    
print (y1, x1)

if random.random() < 0.5:
    y1 += 1 
else:
    y1 -= 1 

if random.random() < 0.5:
    x1 += 1
else:
    x1 -+ 0
    
print (y1, x1)


# Calculate the distance between variables.
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff 

x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff 

sum = y_diffsq + x_diffsq
answer = sum ** 0.5

print (answer)




 