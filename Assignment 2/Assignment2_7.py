def patternPrint(value):
 for x in range(0, value):
  if(x != 0):
   print()
  for x in range(1,value+1):
    print(x,end="   ")


num1 = input("Enter number:")
no1 = int(num1)
patternPrint(no1)