import csv

with open('extrait.csv', newline='') as csvfile:
    # reader = csv.DictReader(csvfile, delimiter='\t')
    reader = csv.reader(csvfile, delimiter='\t')
    k = 0
    for row in reader:
        if k < 100:
            print(row[0], row[1])
        k = k+1


