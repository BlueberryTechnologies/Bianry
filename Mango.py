import random
import tkinter
from tkinter import *
from tkinter.ttk import *
import time

'''
A password generator written in Python developed by
Blueberry Technologies (blueberry.dev)

Maintained and created by:
gh/rileyrichard

This will use Python's random number generator as well as ASCII to generate a random password
'''

def returnNumber():
    replacedValue = userExcludeInput.get().replace(',','')
    currentTimeString = str(time.time()) # Into a string
    if '.' in currentTimeString:
        currentTimeString=currentTimeString.replace('.','')
    last3 = int(currentTimeString[-5:]) % 250
    if last3 >= 122 or last3 <= 65:
        returnNumber()
    else:
        return last3


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
                passwordReceived = returnNumber() #65 and 122
                print(passwordReceived,"is received")
                passwordChar = chr(passwordReceived)
                password[index] = passwordChar
            completedPassword.insert(1.0,''.join(password))
        else:
            completedPassword.insert(1.0,'Please enter a valid number 8-32')
    completedPassword.configure(state='disabled')


rootWindow = tkinter.Tk() # Root level window
rootWindow.geometry("275x250") # Root Window dimensions
rootWindow.title("Mango") # Sets the title of the window

userInput = tkinter.StringVar() # Sets the user input
userExcludeInput = tkinter.StringVar()

'''
Labels, Text and Buttons
'''
characterLimit = Label(rootWindow, text="Character Limit (8-32 Chars)")
userInputEntry = Entry(rootWindow, textvariable=userInput, font=('arial',10))
characterExclude = Label(rootWindow, text="Characters to exclude (CSV)")
userExcludeEntry = Entry(rootWindow, textvariable=userExcludeInput, font=('arial',10))
refreshButton = Button(rootWindow, text="Refresh Password",command=generatePassword)
completedPassword = Text(rootWindow, height=1,width=32)

characterLimit.grid(row=1,column=0, sticky='w')
userInputEntry.grid(row=2,column=0, sticky='w')
characterExclude.grid(row=3,column=0, sticky='w')
userExcludeEntry.grid(row=4, column=0, sticky='w')
refreshButton.grid(row=5,column=0, sticky='w')
completedPassword.grid(row=6,column=0, sticky='w')

# The main loop for displaying the tkinter window
rootWindow.mainloop()