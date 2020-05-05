###################################
#                                 #
#          Sensor Logger          #
#     -=-=-=-=-=-=-=-=-=-=-=-     #
#                                 #
# Author: Marceline Kuo-Arrigo    #
# Created: 17/06/2019             #
# Version: 1.0                    #
#                                 #
###################################


# Testing/Debugging Notes
# * All sections of the code have been tested by running the function seperately with fake data.
#   * For example in a seperate test program.
# * The program has been tested by editing the timer delays to run a lot quicker to ensure there were no errors.
#	* The program was tested at a sleep delay of 0.01 seconds
# * As the code was being written small sections were tested before being put in the program.
#


import datetime
import time
from sense_hat import SenseHat

def intro(): # User Intoduction 
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("     Sensor Logger")
    print("=-=-=-=-=-=-=-=-=-=-=\n\n")

#GrabTemp(), GrabHumi(), GrabPressure(), GrabTime()
# These functions grab the sensor values or a timestamp to be logged, 
# they are in their own seperate function for easy modularity and debugging.
# They will try to grab the data and if it fails for some reason, error out.
def GrabTemp(sense): # Temperature
    try:
        return str(sense.temp)
    except:
        return "Error"
def GrabHumi(sense): # Humidity
    try:
        return str(sense.humidity)
    except:
        return "Error"
def GrabPressure(sense): # Presssure
    try:
        return str(sense.pressure)
    except:
        return "Error"
    
def GrabTime(): # Time
    try:
        return str(datetime.datetime.now().isoformat())
    except:
        return "Error"

def WriteToLog(temp,humi,pressure,timestamp):
    with open('env_data.csv', 'a') as env_data:
            env_data.write(temp+","+humi+","+pressure+","+timestamp+"\n")

def ReadOutLog():
    with open('env_data.csv','r') as env_data:
        return env_data.read()


# loop([sensehat variable])
# This is the main part of the program that loops doing things.
# It adds the sensor and time data together into a string and appends it to a data file.
def loop(sense):
    for x in range(1, 169): # Run only 168 times, there are 168 hours in a hour. Thus run for only a week
        WriteToLog(GrabTemp(sense), GrabHumi(sense), GrabPressure(sense), GrabTime()) # Write Sensor Data
        time.sleep(3600) # Sleep for an hour



# main()
# This functions handles calling other functions and setup of variables such as the SenseHat variable.
def main():
    intro()            # User introduction to program, just a quick statement of program name
    sense = SenseHat() # Creates Sensehat variable 
    loop(sense)        # Begin looping, running logging code
    print(ReadOutLog())# After looping is done, read back the file and print it out to the terminal
    
if __name__ == "__main__":
    main()