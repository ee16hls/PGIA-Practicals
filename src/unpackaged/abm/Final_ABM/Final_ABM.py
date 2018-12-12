# -*- coding: utf-8 -*-
"""
Programming for Geographical Information Analysis: Core Skills 2018
Model run script- Agent Based Model
@author: Hannah Sherwood
"""
"""
This agent-based model has been created using a GUI so that when the code
is run, an additional window will appear. To run the model, users will need to 
click on the model window and select 'run' from a drop down menu at the top of
tool-bar (applicable for a Mac). Once the 'run' option is selected, the model 
will run an animation on the window, with the output (changed environment and 
agent stores) saving to text files.

"""

"""
Imports:
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
Reads in the environment data from a text file
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

# Practice making the environment figures
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
#ax.set_autoscale_on(False)


"""
Reads in x and y values for agents from a webpage
"""
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs = {"class" : "y"})
td_xs = soup.find_all(attrs = {"class" : "x"})
print (td_ys)
print (td_xs)

 
 
"""
Defines agent parameters 
"""
          
num_of_agents = 10
num_of_iterations = 100 
neighbourhood = 20 



"""
Creates the agents using web data
"""

agents = []

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,agents, neighbourhood, y, x))



"""
Sets the frame size of the figure
"""

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True 



"""
Defines the update function for the animation showing agents interaction with the environment
"""
def update(frame_number):
    fig.clear()
    global carry_on
    

    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
 
    # updates the environment plot
    matplotlib.pyplot.imshow(environment)
 
    
    
"""
Moves the agents, gets them to eat the environment and share their food store with neighbours in a set radius
"""

for i in range(num_of_agents):
    agents[i].move()
    agents[i].eat()
    agents[i].share_with_neighbours(neighbourhood)
    
       
    
"""
Calculates the total store of all the agents from one model run
"""
    
totalstore = []
for agent in agents:
        totalstore.append(agent.getstore())
   
     

"""
Final agent stores written to a text file and appended each time the model is run
"""
       
f2 = open("store.txt", 'a')
writer = csv.writer(f2, delimiter = ',')
writer.writerow(totalstore)
f2.close()

   

"""
Plots the agents in the environment 
"""
    
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)

        
    
"""
Stopping conditon initialised
"""
 
if random.random() < 0.01:
    carry_on = False 
    print("stopping condition")
    #print(agents[i]._x, agents[i]._y)
 
       

"""
Defines the gen_function for the animation
"""

def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 100) & (carry_on) :
        yield a 
        a = a + 1 
 
       
"""
Creates the GUI window for the model to run in

"""
root = tkinter.Tk()
root.wm_title("Model")

# animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
# matplotlib.pyplot.show()
  

"""
Defines the 'run' function in the model to begin animation 
"""   

def run():
    global animation 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


"""
Adds a menu bar and 'run' button for users to start the model run
"""

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


"""
Writes out the environment data to a text file
"""

environmentfile = open("environment.txt", 'w')
write = csv.writer(environmentfile, delimiter= ',')
environmentfile.write(str(environment))
environmentfile.close()



tkinter.mainloop() #Waits for interactions.


# for a in agents:
    #for b in agents:
        #distance = distance_between(a, b)
        #a.hi()
        #b.hi()
        #print ("distance", distance)

# print (agents[0]._agents[1]._x)
