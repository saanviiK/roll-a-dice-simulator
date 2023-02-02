from tkinter import *
import random

window = Tk()
 
label = Label(window, font = ('bold', 400)) # label for the dice

def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] # codes for the dots to appear on the dice.
    label.config(text = f'{random.choice(number)}') # random choice selection.
    label.pack() # packing the label so that it will be visible.


window.minsize(600, 600) # for setting the minimum width and height for our window.
window.maxsize(600, 600) # for setting the maximum width and height for our window.

window.title(" ROLL THE DICE!! ") # title for our window.

heading = Label(window, text = " ROLL THE DICE!! ", font = ('bold', 50), bg = 'light cyan') # this will create a label which will appear in our window.
heading.pack(fill = X) # you have to pack this label so that we can see it in our window.

button = Button(window, text = 'Roll', font = ('normal', 25), command = lambda:roll()) # creating a button
button.pack(fill = X) # packing the button so that it is visible.


window.mainloop()