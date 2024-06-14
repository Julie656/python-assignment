# question 12

# Write a python program that calculates the sum of the digit of a given number.

n=int(input("Enter number"))

sum=0

for i in str(n):
    sum=sum+int(i)

print("Sum of digits is: ",sum)


