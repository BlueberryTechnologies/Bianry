import time # To generate the password, we are using time as a seed
def generateAsciiArray(): # Returns a integer based on the current user's time this is between the range of 47 and 126 which is used as common ascii characters
    currTime = None # Sets the current time to None before it's generated
    valueOfTime = 0 # Sets the value of the generated time to 0
    passwordArray = [] # Creates an empty array to store the ascii characters
    password = "" # Creates an empty string to be used as the final placeholder for the user's completed password
    for i in range(32): # Generates a 32 character long randomized password which will be shortened when the user specifies how long they want their password
        while valueOfTime >= 126 or valueOfTime <= 47: # Keeps all values within the range of ascii 47 to 126
            currTime = str(time.time_ns()).replace('0', '') # Removes all zeros from the generated string of the current time
            valueOfTime = int(currTime[-5:]) % 250 # Takes the last 5 digits of time, then mods by 250
        passwordArray.append(chr(valueOfTime)) # Appends the current value of generated time to the end of the array
        valueOfTime = 0 # Resets the value of time to 0
    return passwordArray # Returns the final password

def getGeneratedPassword(specifiedLength):
    if specifiedLength >=8 and specifiedLength<= 32:
        asciiArray = generateAsciiArray() # You have to specify how long you want the password to be
        resizedPasswordString = ""
        for i in range(specifiedLength):
            resizedPasswordString += str(asciiArray[i])
        return resizedPasswordString
    else:
        return "Please enter a number that is between 8 and 32."