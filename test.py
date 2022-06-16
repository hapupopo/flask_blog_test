import csv

with open('cafe-data.csv', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)

for item in range(0, len(list_of_rows)):
    print(item)
    print(list(list_of_rows[item]))


"""
Starbucks
https://goo.gl/maps/5iWJ253yiMWR1gDP6
7:00
10:30
4
5
3


"""