alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 'w','x','y','z']


while(True):
  input1 = input("Enter only either a letter or a number: ")
  try:
    input1 = int(input1)
  except ValueError:
    if input1.lower() in alphabet:
      while(alive):
        input2 = input("Enter a number: ")
        try:
          input2 = int(input2)
        except ValueError:
          print("Error: Not a number")
        else:
          break
      for n in range(0,input2):
        print(input1)
      quit()
    else:
      print("Error: Not a number or single letter")
  else:
    while(True):
      input2 = input("Enter a letter: ")
      if not input2.lower() in alphabet:
        print("Error: Not a single letter")
      else:
        for n in range(0,input1):
          print(input2)
        quit()