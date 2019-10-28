def primeNumber(value):
 for x in range(2,value):
   if(value % x == 0):
      return 0
   else:
      return 1


num1 = input("Enter number:")
no1 = int(num1)
res = primeNumber(no1)
if(res == 0):
  print("It is not prime number")
else:
    print("It is prime number")


