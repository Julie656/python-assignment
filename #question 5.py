#question5

# Write a program that takes the string input from the user and writes to the text file

fname = input("Enter file name: ")
user_input = input("Enter string to append: ")
try:
    with open(fname, "a") as file:
        file.write(user_input + '\n')
except Exception as e:
    print("There is a problem:", str(e))