import csv

input_file = csv.reader(open('./bundesliga-2014-2015-game.csv' , 'r', encoding='utf-8'))

data = next(input_file)

index = 0
for item in data:
    print(str(index) + " " + item)
    index = index + 1