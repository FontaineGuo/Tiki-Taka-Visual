import csv
from data_process import config
import os
current_path = os.path.dirname(__file__)

def get_pts(leaguename, year):
    path = config.table_root_path[leaguename]
    csv_data = csv.reader(open(current_path + path + config.nameDict[leaguename] + '-' + year + '-table.csv' , 'r', encoding='utf-8'))
    # return path + config.nameDict[leaguename] + '-' + year + '-table.csv'
    pts_table = ''
    for _index, data in enumerate(csv_data):
        for item in data:
            pts_table = pts_table + ' ' + str(item)
        pts_table = pts_table + '\n'
    # return csv_data
    return pts_table


# print(get_pts('Premier League', '2010-2011'))