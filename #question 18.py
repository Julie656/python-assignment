#question 18

# Write a python program that checks if two strings are anagrams of each other.

string_1=input("enter the first screen: ")
string_2=input("enter the second screen: ")
if(sorted(string_1)==sorted(string_2)):
    print("strings are anagrams")
else:
    print("the strings aren't anagrams")