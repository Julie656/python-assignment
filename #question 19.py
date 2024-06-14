#question 19

# Write apython program that removes all punchuation from a given string.

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str_1=input("enter the string: ")


no_punct = ""
for i in str_1:
   if i not in punctuations:
       no_punct = no_punct + i
print(no_punct)
