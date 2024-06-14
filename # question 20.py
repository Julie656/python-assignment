# question 20

#Write a python program that takes the list of numbers and return their sum.

def sum(numbers):
    total = 0
    
    for i in numbers:
        
        total += i
    
    return total
print(sum((8, 2, 3, 0, 7))) 
