import csv
import re

# filename = 'test.csv'
# with open(filename, 'w') as f:
#             csv_writer = csv.writer(f, delimiter=',' ,lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
#             # write title
#             csv_writer.writerow(['player', 'country', 'team', 'goal', 'penalty'])
#             csv_writer.writerow([1, 2, 3, 4, 5])
#             csv_writer.writerow([1, 2, 3, 4, 5])
#             csv_writer.writerow([1, 2, 3, 4, 5])

# ab = [1,2,3,4,5,6]

# for n in ab[1:]:
#     print(n)

# pattern = r'\((\d{0,2})\)'

# print(re.search(pattern, '\'  (16)\'')[1])

# link = 'https://www.worldfootball.net/goalgetter/eng-premier-league-2010-2011/'
# name_group = link.split('/')
# print(name_group[-2]+'-'+ name_group[-3])

l1 = ['a','b', 'c']
l2 = ['d', 'e']
l1.extend(l2)
print(l1)