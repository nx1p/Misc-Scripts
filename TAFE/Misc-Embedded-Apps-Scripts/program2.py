numList = []
Alive = True

print("=-=-=-=-=-=-=-=-=-=-=")
print("Enter at least ten numbers, enter 'stop' when you're done")
print("=-=-=-=-=-=-=-=-=-=-=")
while(Alive):
  while(True):
    UserInput = input("Enter a number: ")
    try:
      if 'stop' in UserInput:
        if len(numList) >= 10:
          Alive=False
          break
        elif len(numList) <= 10:
          print("You need to enter at least 10 numbers before stopping")
      else:
        numList.append(int(UserInput))
    except ValueError:
      print("error: You didn't enter a number or 'stop', enter a number or stop")
    except:
      print("error: Unknown general error")
    else:
      break

print("List: " + str(numList))
print("Sum of list: "+str(sum(numList)))