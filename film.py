import csv

titles = {}

with open('films.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        Title = row['Title']
        if Title in titles:
            titles[Title] += 1
        else:
            titles[Title] = 1

for Title in sorted(titles):
    print(Title, titles[Title])
    