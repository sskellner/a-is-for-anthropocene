import csv
from random import choice
import time

items = []
places = []
years = []

wayshere = [
    'donated by an elderly couple',
    'donated by a private gallery',
    'purchased at an auction for very little',
    'purchased from an art collector for a hefty price',
    'borrowed from another museum',
    'taken from an older exhibit upstairs',
    'stolen in the previous century'
    ]

alternatives = [
    'sold to someone else',
    'sold in an estate sale',
    'destroyed in the next war',
    'lost along the way',
    'thrown in a landfill',
    'the same place it started'
]

with open('longnowdata.csv', encoding='utf-8-sig') as mycsv:
    csv_reader = csv.reader(mycsv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        items.append(row[0])
        places.append(row[1])
        years.append(row[2])

# (item name)
# it comes from (place)
# to get to this museum, it was (wayshere)
# if it wasn't here, it would have been (alternatives)


def getentry(index):
    print(items[index])
    print('It came from ' + places[index] + '.')
    print('It arrived at this museum in ' + years[index] + '.')
    print('To get to this museum, it was ' + choice(wayshere) + '.')
    print('If it wasn\'t here, it would have been ' + choice(alternatives) + '.')


s = 0

while s < 26:
	getentry(s)
	s += 1

	time.sleep(5)
