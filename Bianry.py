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

import Generate # /Generate.py
import customtkinter # https://github.com/TomSchimansky/CustomTkinter
import pyperclip # https://pypi.org/project/pyperclip/


asciiString = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@[]^_`{|}~:;<=>?/\\"

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

binary = customtkinter.CTk()
binary.geometry("800x480")
binary.title("Bianry")

userGeneratedPassword = ""


def generatePassword():
    passwordEntry.delete(0, 32)
    global userGeneratedPassword
    try:
        userDefinedLength = int(userEntry.get())
        userDefinedExclusion = exclusionEntry.get()
        userGeneratedPassword = Generate.getGeneratedPassword(userDefinedLength, userDefinedExclusion)
        if userGeneratedPassword == -1:
            warnings.configure(text="Please enter a number that is between 8 and 32.")
        else:
            warnings.configure(text="")
            passwordEntry.insert(0, userGeneratedPassword)
    except ValueError:
        warnings.configure(text="Please enter a number that is between 8 and 32.")
    

def copyToClipboard():
    if userGeneratedPassword is not None:
        print("The password is: " + userGeneratedPassword)
        pyperclip.copy(userGeneratedPassword)
    else:
        print("There is nothing to copy")


warnings = customtkinter.CTkLabel(binary, text="", width=200)
userEntry = customtkinter.CTkEntry(binary, width=200, placeholder_text="Enter length of password 8-32")
exclusionEntry = customtkinter.CTkEntry(binary, width=200, placeholder_text="Enter excluded characters")
submitButton = customtkinter.CTkButton(master=binary, width=200, text="Submit", command=generatePassword)
copyButton = customtkinter.CTkButton(master=binary, width=200, text="Copy to Clipboard", command=copyToClipboard)
passwordEntry = customtkinter.CTkEntry(binary, width=200)


warnings.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
userEntry.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
exclusionEntry.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
submitButton.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
copyButton.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
passwordEntry.place(relx=0.5,rely=0.7, anchor=customtkinter.CENTER)

binary.mainloop()