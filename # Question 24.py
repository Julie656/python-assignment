# Question 24

# Write a python program that acts as a simple calculator . It can take two numbers and perform (+,-,%,*) as inputs and print the result.
user=input()
num1=int(input("enter the  first number: "))
num2=int(input("enter the second number: "))
sum =0
difference=0
product=1
division=1
if(user=='+'):
    sum=num1+num2
    print("sum is: ",sum)
elif(user=='-'):
    difference=num1-num2
    print("difference is: ",difference)
elif(user=='*'):
    product=num1*num2
    print("product of two numbers is: ",product)
elif(user=='%'):
    division=num1%num2
    print("the division of two numbera is: ",division)
else:
    print("please take the correct operators!!")




