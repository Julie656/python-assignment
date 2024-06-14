# question 14

# Write a python program that reads multiple lines of input from the user until they enter the empty line,
# then prints all the line.
 
lines = [] 

while True: 
    line = input("Enter a line (leave empty to finish): ") 
    if line: 
        lines.append(line) 
    else: 
        break
multiline_input = '\n'.join(lines) 
 
print("Multiline input:") 
print(multiline_input) 

  