import random

'''
A password generator written in Python developed by
Blueberry Technologies (blueberry.dev)

Maintained and created by:
gh/rileyrichard

This will use Python's random number generator as well as ASCII to generate a random password

'''
def userInput():
    print("Welcome to the Password Generator")
    numChars = input("Please enter the number of characters for your password.\n> ")
    return int(numChars)

def generatePassword(numberOfCharacters):
    password = [None] * numberOfCharacters
    for index, values in enumerate(password):
        passwordNum = random.randint(65,122)
        passwordChar = chr(passwordNum)
        password[index] = passwordChar
    return ''.join(password)
print(generatePassword(userInput()))