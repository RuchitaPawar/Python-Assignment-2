def patternPrint(value):
 for x in range(1, value+1):
  if (x != 0):
   print()
   for y in range(1,x+1):
    print(y,end="   ")

num1 = input("Enter number:")
no1 = int(num1)
patternPrint(no1)