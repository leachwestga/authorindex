

import csv
file = open('authorlist.csv')
reader = csv.reader(file)
author={}

for line in reader:
    print(line)
    author[int(line[0])] = line[1].strip() + ", " + line[2].strip()

for i in range(100):
    print(author[17*i+1])
    

