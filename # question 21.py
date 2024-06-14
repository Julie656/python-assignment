# question 21

# write a python program that counts the occurence of specific elements in a given list.

list=eval(input("enter the element of list: "))
element_to_count = 1
count = len([i for i in list if i == element_to_count])
print(f"The element {element_to_count} occurs {count} times")


