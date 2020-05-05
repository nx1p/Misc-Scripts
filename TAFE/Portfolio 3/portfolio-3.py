########################################
#                                      #
#   Sensor Logger Chart Generator      #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  #
#                                      #
# Author: Marceline Kuo-Arrigo         #
# Created: 17/06/2019                  #
# Version: 0.8                         #
#                                      #
########################################

import pygal

def intro(): # User Intoduction 
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("     Log Data Chart Generator")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")

# Set the desired settings for pygal, give it the data and render chart to a file
def GenerateChart(temp, humi, pressure, timestamp):
    line_chart = pygal.Line(height=1080, width=1920, x_title='Time', y_title='Sensor Data', human_readable=True)
    line_chart.title = 'Sensor Log Data'
    line_chart.x_labels = timestamp
    line_chart.add('Temperature', temp)
    line_chart.add('Humidity',  humi)
    line_chart.add('Pressure',pressure)
    line_chart.render_to_file('line_chart.svg') 

#main()
# This is the main function. It contains most of the code such as the code that opens and parses the log data file.
def main():
    intro()
    print("...")
    
    #Read sensor log data lines into an array
    try:
        data = open("env_data.csv").read().splitlines()
    except:
        print("Error: Failed opening log data, please check log data is there and not intact")
    print(" > Log Data read into memory.")
    
    
    # initalise the array varriables 
    temp = []
    humi = []
    pressure = []
    timestamp = []
    
    # run through the lines and seperate the data into their own varriables
    for line in data:
        try:
            splitted=line.split(',')
            temp.append(float(splitted[0]))
            humi.append(float(splitted[1]))
            pressure.append(float(splitted[2]))
            timestamp.append(splitted[3])
        except:
            print("Error: Failed parsing the log data, please double check log data isn't corrupt")
    print(" > Log Data parsed.")
    
    
    try:
        GenerateChart(temp, humi, pressure, timestamp)
    except:
        print("Sorry there was an error generating the chart")
    print(" > Chart has been successfully generated.")


if __name__ == "__main__":
    main()