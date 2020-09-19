#Coloring and Styling ipywidgets
#ipywidgets has switched over to a Bootstrap style

#https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Styling.html#Predefined-styles


from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

#Create Basic Interact function
#Interact auto-generates a user interface control for some sort of function argument
#and then it calls the function with these arguments that we can allow ourselves to
#manipulate interactively

def func(x):
    return x

interact(func,x=10)         #Slider
interact(func,x='Hello')    #Text box
interact(func,x=True)       #Check box

@interact(x=True,y=1.0)     #x - Check box
def g(x,y):                 #y - Slider
    return (x,y)