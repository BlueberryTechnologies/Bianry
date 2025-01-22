import Generate
#import Embed

# To render the UI tkinter is needed
import tkinter
from tkinter import *
from tkinter.ttk import *


'''
A password generator for stronger passwords written in Python developed by
Blueberry Technologies (blueberry.dev)

Maintained and created by:
gh/rileyrichard
gh/tehsavi0r

With help from all at Blueberry Technologies

'''

def getGeneratedPassword():
    completedPassword.configure(state='normal')
    
    if userInput.get() == "":
        completedPassword.insert(1.0,"Please enter a number")
    else:
        try:
            numberOfCharacters = int(userInput.get())
            if numberOfCharacters >= 8 and numberOfCharacters <= 32:
                asciiString = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@[]^_`{|}~:;<=>?/\\"
                countedInt = 0
                for values in userExcludeInput.get():
                    if values in asciiString:
                        countedInt += 1
                        print("Counted int is:",countedInt)
                if countedInt == 80:
                    userPassword = "nice try"
                else:
                    userPassword = ""
                    for i in range (numberOfCharacters):
                        userPassword = "".join(Generate.generateAsciiArray(i))
                completedPassword.delete(1.0,'end')
                completedPassword.insert(1.0,userPassword)
            else:
                completedPassword.insert(1.0,'Please enter a valid number 8-32')
        except ValueError:
            completedPassword.insert(1.0,'Please enter only integer values.')
    completedPassword.configure(state='disabled')



rootWindow = tkinter.Tk() # Root level window
rootWindow.geometry("275x250") # Root Window dimensions
rootWindow.title("Bianry") # Sets the title of the window

userInput = tkinter.StringVar() # Sets the user input
userExcludeInput = tkinter.StringVar()

'''
Labels, Text and Buttons
'''
characterLimit = Label(rootWindow, text="Character Limit (8-32 Chars)")
userInputEntry = Entry(rootWindow, textvariable=userInput, font=('arial',10))
characterExclude = Label(rootWindow, text="Characters to exclude")
userExcludeEntry = Entry(rootWindow, textvariable=userExcludeInput, font=('arial',10))
refreshButton = Button(rootWindow, text="Refresh Password",command=getGeneratedPassword)
completedPassword = Text(rootWindow, height=1,width=32)

characterLimit.grid(row=1,column=0, sticky='w')
userInputEntry.grid(row=2,column=0, sticky='w')
characterExclude.grid(row=3,column=0, sticky='w')
userExcludeEntry.grid(row=4, column=0, sticky='w')
refreshButton.grid(row=5,column=0, sticky='w')
completedPassword.grid(row=6,column=0, sticky='w')

# The main loop for displaying the tkinter window
rootWindow.mainloop()