#import libraries
import csv

#ask user for title, strip and convert to uppercase to help 
# with comparison
title = input('Title: ').strip().upper()

#set counter to 0
counter = 0

#open file and read it as a dictionary and iterate through
# it to find the title and increment the counter by 1 if found
with open('films.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        Title = row['Title'].strip().upper() == title
        counter += 1

#output the counter
print(counter)
