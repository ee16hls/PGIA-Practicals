# Programming for Geographical Information Analysis: Core Skills 

This repository contains code written for the Module GEOG 5990M with the School of Geography at the University of Leeds. The aim of the module was to introduce students to coding with the Python Programming language and classes involved building a simple Agent Based Model (ABM). In this repository you will find versions of code from each practical class which builds on from the next to produce the final Agent Based Model (see **Final_ABM.py**).

The model itself has been created to simulate simple behaviours in agents which occur within an environment read in from a **CSV file** (in.text). Behaviours include moving around the environment, eating the environment and sharing a store of 'food' with other agents within a set radius. The model has followed an **'object orientated approach'** and thus has involved the creation of an Agent **class** which has a pre-defined the set of behaviours for all of the Agents (see **AgentFramework.py**). 

When the model is run, the agents will 'eat'the 2D raster environment they are moving around in, therefore the output file of this ABM (the **environment.txt** file) will save the changed/nibbled environment data and append the file for each model run. Similarly the text file **store.txt** saves the total store of food from all the agents after the model has run. 


# Running the Code 

This agent-based model has been created using a GUI so that when the code is run, an additional window will appear. To run the model, users will need to click on the model window and select 'run' from a drop down menu at the top of tool-bar (applicable for a Mac). Once the 'run' option is selected, the model will run an animation on the window, with the output, changed environment and total agent stores from each run, saving to the text files **environment.text** and **store.txt**.
