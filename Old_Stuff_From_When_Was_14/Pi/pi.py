import math
import time

#This script uses the fact that the more sides a regular polygon has, the closer to a circle it and thus it's perimeter gets

#Function: From the a known number of sides, calculate the length from the midpoint of a side to the center of the polygon
def CalculateApothem(numberSides):
    sideLength = 1.0
    return sideLength / ((math.tan(math.radians(180 / numberSides))) * 2)

#Function: Using the number of sides and assuming each side is 1 unit long, calculate and return the result which is the perimeter
def CalculatePerimeter(numberSides):
    sideLength = 1.0
    return sideLength * numberSides

#Function: From the a known number of sides, calculate the ratio of a regular polygon's perimeter to its diameter
def CalculateTheThingForXSides(numberSides):
    perimeter = CalculatePerimeter(numberSides)
    apothem = CalculateApothem(numberSides)
    TheresProbablyATermForThisIDontKnow = perimeter / (apothem * 2)
    return TheresProbablyATermForThisIDontKnow

numberSides = 0.0
calculatedPi = 0.0

start = time.time() # Get timestamp before start of calculations

#If calculated pi rounded to ~~4~~ 10 decimals places isn't equal to Pi rounded to 4 points then loop and recalculate increasing the number of sides
while(round(calculatedPi,10) != round(math.pi,10)):
    numberSides += 1.0 #Increase current number of sides by 1
    calculatedPi = CalculateTheThingForXSides(numberSides)
    print "\nCurrently calculating the perimeter of a regular polygon with:                  " + str(numberSides)+" sides"
    print "The ratio of a regular polygon with "+str(numberSides)+" sides's perimeter to its diameter is: " + repr(calculatedPi)

print "\nCalculated : " + repr(calculatedPi)
print "Pi         : " + repr(math.pi)
print "Took       : " + repr(time.time() - start) + " Seconds"
