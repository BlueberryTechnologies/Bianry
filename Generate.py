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
# Imports
import time


'''
generateAsciiArray

Generates random numbers based off of the time seed then converts to the number's ascii value then places in an array.
This function generates 32 characters by default.
'''
def generateAsciiArray():
    currTime = None
    valueOfTime = 0
    passwordArray = []
    password = ""
    for i in range(32):
        while valueOfTime >= 126 or valueOfTime <= 47:
            currTime = str(time.time_ns()).replace('0', '')
            valueOfTime = int(currTime[-5:]) % 250
        passwordArray.append(chr(valueOfTime))
        valueOfTime = 0 
        time.sleep(.001)
    return passwordArray 



'''
getGeneratedPassword

Generates a string based off of the array of chars generated in generateAsciiArray.
This also takes a specifiedLength variable into account as the user specifies which length they would like.
'''
def getGeneratedPassword(specifiedLength):
    if specifiedLength >=8 and specifiedLength<= 32:
        asciiArray = generateAsciiArray()
        resizedPasswordString = ""
        for i in range(specifiedLength):
            resizedPasswordString += str(asciiArray[i])
        return resizedPasswordString
    else:
        return -1