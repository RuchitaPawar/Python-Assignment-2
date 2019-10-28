def addDigit(value):
 sum=0
 while(value > 0):
  digit = value % 10
  value = value//10
  sum = sum + digit

 return sum

num1 = input("Enter number:")
no1 = int(num1)
res = int (addDigit(no1))
print("Total of digits in number is",res)


