import csv
import config


def get_pts(leaguename, year):
    path = config.table_root_path[leaguename]
    input_file = csv.reader(open(path + config.nameDict[leaguename] + '-' + year + '-table.csv' , 'r', encoding='utf-8'))
    # return path + config.nameDict[leaguename] + '-' + year + '-table.csv'
    for _index, data in enumerate(input_file):
        print(data)

print(get_pts('Premier League', '2010-2012'))