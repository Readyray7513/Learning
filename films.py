import csv

titles = {}

with open('films.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        Title = row['Title'].strip().upper()
        if Title in titles:
            titles[Title] += 1
        else:
            titles[Title] = 1

def get_value(Title):
    return titles[Title]

for Title in sorted(titles, key=get_value, reverse=True):
    print(Title, titles[Title])

