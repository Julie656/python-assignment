# question 9
# Write a python program that checks if a substring  is present in a given string

string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")
if(substring in string):
    print("yes!", substring , "is present")
else:
    print(substring," is not present")
    
