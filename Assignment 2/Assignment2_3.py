def factorial(number):
  fact =1
  while(number > 0):
    fact = fact * number
    number = number-1
  return fact

num1 = input("Enter number:")
no1 = int(num1)
res = factorial(no1)
print(res)