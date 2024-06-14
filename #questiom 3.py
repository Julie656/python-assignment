#questiom 3

#wRITE A PYTHON PROGRAM  THAT CALCULATES THE FACTORIAL OF A NUMBER

num=int(input("enter the number: "))
fact=1
if(num<0):
    print("factorial of negative number doesnot exist")
elif(num==0):
    print("factorial of zero is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,"is: ",fact)