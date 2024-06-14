# Question 22

#Write a python program that returs the miniumum and maximum value from a given list.

def find_min_max(list):
    if not list:
        return None, None  # Return None for empty lists
    return min(list), max(list)

my_list = [5, 2, 8, 1, 9, 3]
minimum, maximum = find_min_max(my_list)

print(f"The minimum value is {minimum}")
print(f"the maximum value is {maximum}")