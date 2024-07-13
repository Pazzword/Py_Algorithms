import csv


with open('example.txt', 'a') as file:
    file.write('This is an appended line.\n')


new_data = [
    ['David', 40, 'Houston'],
    ['Eva', 28, 'Boston']
]

with open('example.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_data)