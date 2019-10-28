def countDigit(value):
 count = 0
 while(value > 0):
     value = value // 10
     count = count + 1
 return count

num1 = input("Enter number:")
no1 = int(num1)
res = countDigit(no1)
print("Number of digits are",res)


