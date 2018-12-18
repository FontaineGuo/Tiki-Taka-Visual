import sqlite3
import json
import pandas as pd
from collections import OrderedDict


year_lst = ["2010-2011", "2011-2012", "2012-2013", "2013-2014", "2014-2015", "2015-2016", "2016-2017", "2017-2018"]
conn = sqlite3.connect('./DataSrc/game.db')

cursor = conn.cursor()
# matches = pd.read_sql_query("SELECT * from bundesliga_game limit 0,1", conn)
cursor.execute("SELECT * from premierleague_game")


dic_list = []
index = 1
year_index = 0
round_index = 1
for item in cursor:
    if index == 3041:
        break
    temp_dict = OrderedDict()
    temp_dict['season'] = year_lst[year_index]
    temp_dict['home'] = str(item[2])
    temp_dict['away'] = str(item[3])
    temp_dict['id'] = int(index-1)
    temp_dict['round'] = round_index
    dic_list.append(temp_dict)
    if index % 10 == 0:
        round_index = round_index + 1
    if index % 380 == 0:
        print(year_lst[year_index])
        round_index = 1
        year_index = year_index + 1
        index = index + 1
    else:
        index = index + 1
cursor.close()
j = json.dumps(dic_list)
with open('premierleague_game.json', 'w') as f:
    f.write(j)