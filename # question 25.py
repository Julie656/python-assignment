# question 25

# Write  a python progam  that copies the contents of one text file to another.

first_file=open("first.txt","r")
second_file=open("second_file.txt","w")
for i in first_file:
    second_file.write(i)
    print("second file is: ",i)