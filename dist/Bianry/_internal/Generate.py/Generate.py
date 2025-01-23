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

Generates random numbers based off of the time seed then converts to the number's ascii value.
'''

def generateAsciiChar():
    currTime = None
    valueOfTime = 0
    asciiValueOfTime = ""
    while valueOfTime >= 126 or valueOfTime <= 47:
        currTime = str(time.time_ns()).replace('0', '')
        valueOfTime = int(currTime[-5:]) % 250
        asciiValueOfTime = chr(valueOfTime)    
        time.sleep(.001)
    return asciiValueOfTime

'''
getGeneratedPassword

Generates a string based off of the array of chars generated in generateAsciiArray.
This also takes a specifiedLength variable into account as the user specifies which length they would like.
'''
def getGeneratedPassword(specifiedLength, excludedCharacters):
    asciiString = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@[]^_`{|}~:;<=>?/\\"
    niceTryCount = 0
    for i in range(len(asciiString)):
        if asciiString[i] in excludedCharacters:
            niceTryCount += 1
    
    if niceTryCount == 80:
        return "Nice Try"

    asciiArray = []
    if specifiedLength >=8 and specifiedLength<= 32: # Within bounds
        for i in range(specifiedLength):
            asciiArray.append(generateAsciiChar())
            for i in range(len(asciiArray)):
                while asciiArray[i] in excludedCharacters:
                    asciiArray[i] = generateAsciiChar()
        asciiString = ''.join(asciiArray)
        return asciiString
    else:
        return -1