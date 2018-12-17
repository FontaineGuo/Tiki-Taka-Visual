import pandas
import csv, sqlite3
conn= sqlite3.connect("./process/seriea_game.db")
years = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015',
        '2015-2016', '2016-2017', '2017-2018']
for year in years:
    print(year)
    seasonData = pandas.read_csv('./process/seriea-'+ year +'-game.csv')
    seasonData.to_sql('seriea_game', conn, if_exists='append', index=False)

print('ok')