from sense_hat import SenseHat
ValidColours = ["R", "G", "B", "W"]
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)


def intro(): 
    print("=-=-=-=-=-=-=-=-=-=-=")
    print("Enter a XY coordinate and colour\n")
    print("Use this format: 'X:Y|<colour>' ")
    print("Where colour can either be a R, G, B or W.")
    print("Red, Green, Blue, White respectively")
    print("Example input: \"0:0|R\"")
    print("\nEnter \"X\" to exit at any time")
    print("=-=-=-=-=-=-=-=-=-=-=")
    
def DisplayGenericFormatError(): #Display a generic format error asking user to use the proper format
    print("Error: Please use use this format: 'X:Y|<R,G,B or W>'")
    
#Loop and continue to ask for more user input unless user instructs program to exit
def loop(sense): 
    while(True):
        UINPUT = input(">    ")
        if UINPUT.upper() == "X":
            print("=-=-=-=-=")
            print(" Exiting")
            print("=-=-=-=-=")
            break
        if not ( ('|' in UINPUT) and (':' in UINPUT) ):
            DisplayGenericFormatError()
        else:
            ARGS = UINPUT.split("|")
            if len(ARGS) != 2:
                DisplayGenericFormatError()
            elif len(ARGS) == 2:
                if len(ARGS[0].split(":")) != 2:
                    DisplayGenericFormatError()
                elif len(ARGS[0].split(":")) == 2:
                    try:
                        COORDS = {
                            "X" : int(ARGS[0].split(":")[0]),
                            "Y" : int(ARGS[0].split(":")[1])
                        }
                    except ValueError:
                        print("Error: Coordinates must be an integer")
                    else:
                        if ( (COORDS["X"] >= 0) and (COORDS["X"] <= 7) ) and ( (COORDS["Y"] >= 0) and (COORDS["Y"] <= 7) ):
                            if len(ARGS[1].upper()) != 1:
                                DisplayGenericFormatError()
                            elif len(ARGS[1].upper()) == 1:
                                if ARGS[1].upper() not in ValidColours:
                                    print("Error: Colour must be Red, Green, Blue or White")
                                elif ARGS[1].upper() in ValidColours:
                                    COLOUR_str = ARGS[1].upper()
                                    PotentialColours = {'R': red, 'G': green, 'B': blue, 'W': white}
                                    COLOUR = PotentialColours.get(COLOUR_str)
                                    sense.set_pixel(COORDS["X"], COORDS["Y"], COLOUR)
                        else:
                            print("Error: Coordinates must be between 0 and 7")
                            
                    
                    


def main():
    intro() #Instruct user in how to use program and what the program does
    sense = SenseHat()
    loop(sense) #Begin looping
    quit() # Quit if user broke the loop

if __name__ == "__main__":
    main()