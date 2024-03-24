import random
import os
import tkinter
from tkinter import *
from tkinter.ttk import *

'''
A password generator written in Python developed by
Blueberry Technologies (blueberry.dev)

Maintained and created by:
gh/rileyrichard

This will use Python's random number generator as well as ASCII to generate a random password

'''
def generatePassword():
    completedPassword.configure(state='normal')
    completedPassword.delete(1.0,'end')
    if userInput.get() == "":
        completedPassword.insert(1.0,"Please enter a number")
    else:
        numberOfCharacters = int(userInput.get())
        if numberOfCharacters > 7 and numberOfCharacters < 33:
            password = [None] * numberOfCharacters
            for index, values in enumerate(password):
                passwordNum = random.randint(65,122)
                passwordChar = chr(passwordNum)
                password[index] = passwordChar
            completedPassword.insert(1.0,''.join(password))
        else:
            completedPassword.insert(1.0,'Please enter a valid number 8-32')
    completedPassword.configure(state='disabled')


rootWindow = tkinter.Tk() # Root level window
rootWindow.geometry("275x250") # Root Window dimensions
rootWindow.title("Mango") # Sets the title of the window

userInput = tkinter.StringVar() # Sets the user input


'''
Labels, Text and Buttons
'''
characterLimit = Label(rootWindow, text="Character Limit (8-32 Chars)")
userInputEntry = Entry(rootWindow, textvariable=userInput, font=('arial',10))
refreshButton = Button(rootWindow, text="Refresh Password",command=generatePassword)
completedPassword = Text(rootWindow, height=1,width=32)

characterLimit.grid(row=1,column=0, sticky='w')
userInputEntry.grid(row=2,column=0, sticky='w')
refreshButton.grid(row=3,column=0, sticky='w')
completedPassword.grid(row=4,column=0, sticky='w')


# The main loop for displaying the tkinter window
rootWindow.mainloop()