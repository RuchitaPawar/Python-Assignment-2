def factor(number):
  sum = 0;
  for x in range(1,number):
    if(number % x == 0):
        sum = sum + x
  return sum

num1 = input("Enter number:")
no1 = int(num1)
res = factor(no1)
print(res)