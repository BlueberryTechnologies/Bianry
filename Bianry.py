'''
______ _                        
| ___ (_)                       
| |_/ /_  __ _ _ __  _ __ _   _ 
| ___ \ |/ _` | '_ \| '__| | | |
| |_/ / | (_| | | | | |  | |_| |
\____/|_|\__,_|_| |_|_|   \__, |
                           __/ |
                          |___/ 

A password generator for much stronger passwords written in Python developed by
Blueberry Technologies (https://blueberry.dev)

Based off of the forked project Mango (https://blueberry.dev/projects/mango)

Maintained and created by:
gh/rileyrichard
gh/tehsavi0r
'''

import Generate
import customtkinter # https://github.com/TomSchimansky/CustomTkinter
import pyperclip


asciiString = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@[]^_`{|}~:;<=>?/\\"

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")
userGeneratedPassword=""

def generatePassword():
    userDefinedLength = int(userEntry.get())
    userGeneratedPassword = Generate.getGeneratedPassword(userDefinedLength)
    passwordEntry.configure(text=userGeneratedPassword)
    print(userGeneratedPassword)

def copyToClipboard():
    if userGeneratedPassword is not None:
        pyperclip.copy(userGeneratedPassword)
    else:
        print("There is nothing to copy")

userEntry = customtkinter.CTkEntry(app, placeholder_text="Enter length of password 8-32")
submitEntry = customtkinter.CTkButton(master=app, text="Submit", command=generatePassword)
passwordEntry = customtkinter.CTkLabel(app, text="")
copyButton = customtkinter.CTkButton(master=app, text="Copy to Clipboard", command=copyToClipboard)
userEntry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
passwordEntry.place(relx=0.5,rely=0.3, anchor=customtkinter.CENTER)
submitEntry.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
copyButton.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)


app.mainloop()