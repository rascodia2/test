import csv

with open('catalog.csv', 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    print(type(reader))
    for fila in reader:
        print(fila[1])