#   Question 16

# Write a program in python that counts the frequency of each character in a string.
str1="hello guys"

# create dictionary to store key value pair
dict = {}

for i in str:
    
    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1

print(dict)