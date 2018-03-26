import csv

with open('example.csv') as f:
    rows = csv.reader(f, delimeter=',')
    header = next(rows);
    
    for row in rows:
        print(row)
