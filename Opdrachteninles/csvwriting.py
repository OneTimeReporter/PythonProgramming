import csv

with open('newfile.csv', 'w', newline='') as myCSVFFile:
    writer = csv.writer(myCSVFFile, delimiter=';')
    writer.writerow(('number', 'name'))

    while True:
        name = input('Name?')

        if name == '':
            break
        number = input('Number?')

        writer.writerow((number,name))


        