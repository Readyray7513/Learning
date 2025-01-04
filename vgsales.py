import csv

titles = {}

with open('films.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row['title'].strip().upper()
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 0

for title in sorted(titles):
    print(title)