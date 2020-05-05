while(True): #Num 1, loops back and ask for number again if exception happens 
  try:
    num1_int = int(input("Number 1: "))
  except ValueError:
    print("error: Not a number, enter a number")
  except:
    print("error: Unknown general error")
  else:
    break
  
#Asks for operator, makes sure two operators are not put in at once
#Will loops back and asks again if there are no operators or multiple operates
#were put in
while(True):  
  operator = input("Operator: (*, /, +, -)")
  if ('*' in operator) and ('-' not in operator) and ('+' not in operator) and ('/' not in operator):
    operator = "*"
    break
  elif ('/' in operator) and ('-' not in operator) and ('+' not in operator) and ('*' not in operator):
    operator = "/"
    break
  elif ('+' in operator) and ('-' not in operator) and ('/' not in operator) and ('*' not in operator):
    operator = "+"
    break
  elif ('-' in operator) and ('+' not in operator) and ('/' not in operator) and ('*' not in operator):
    operator = "-"
    break
  elif ('-' not in operator) and ('+' not in operator) and ('/' not in operator) and ('*' not in operator):
    print("error: no operators detected")
  else:
    print("error: Not a valid response, did you put in two operators?")
    
    
#Num 2, loops back and ask for number again if exception happens 
while(True):
  try:
    num2_int = int(input("Number 2: "))
  except ValueError:
    print("error: Not a number, enter a number")
  except:
    print("error: Unknown general error")
  else:
    break
  
  

try:
  if operator == "*":
    print("Result: "+str(num1_int*num2_int))
  elif operator == "/":
    print("Result: "+str(num1_int/num2_int))
  elif operator == "+":
    print("Result: "+str(num1_int+num2_int))
  elif operator == "-":
    print("Result: "+str(num1_int-num2_int))
except ZeroDivisionError:
  print("Error: Cannot divide by zero")

