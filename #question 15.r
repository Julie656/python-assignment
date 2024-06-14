#question 15

# Write a program that reads data from csv file and prints it to the console

import csv

# Open the CSV file in read mode
with open('practice.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
