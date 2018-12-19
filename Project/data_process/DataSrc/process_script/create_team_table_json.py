import sqlite3
import json
from collections import OrderedDict

years = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015',
        '2015-2016', '2016-2017', '2017-2018']
conn = sqlite3.connect('..\\league_table.db')
cursor = conn.cursor()

leagues = ['bundesliga', 'laliga','seriea', 'ligue1', 'premierleague']

for league in leagues:
    team_yearDict = OrderedDict()
    for year in years:
        print('processing ' + year)
        cursor.execute("SELECT Team from '" + league + "_" + year + "_table'")
        team = []
        for item in cursor:
            if str(item[0]) in team_yearDict:
                temp_list = team_yearDict[str(item[0])]
                temp_list.append(year)
                team_yearDict[str(item[0])] = temp_list
            else:
                team_yearDict.update({str(item[0]):[]})
                team_yearDict[str(item[0])].append(year)
    j = json.dumps(team_yearDict)
    with open(league + '_team_season.json', 'w') as f:
        f.write(j)
