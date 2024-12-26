import csv

titles = {}

with open('films.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        Title = row['Title'].strip().upper()
        if Title in titles:
            titles[Title] += 1
        else:
            titles[Title] = 0

for Title in sorted(titles):
    print(Title)