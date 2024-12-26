import csv

name = input('Enter name: ')
phone = input('Enter phone: ')

with open('phonebook.csv', 'a') as file:

    writer = csv.writer(file)
    writer.writerow([name, phone])
