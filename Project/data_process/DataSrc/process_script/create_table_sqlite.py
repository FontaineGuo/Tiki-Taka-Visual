import pandas
import csv, sqlite3
conn= sqlite3.connect("./league_table.db")
years = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015',
        '2015-2016', '2016-2017', '2017-2018']
for year in years:
    print(year)
    seasonData = pandas.read_csv('./process/laliga-'+ year +'-table.csv')
    seasonData.to_sql('laliga_' + year+ '_table', conn, if_exists='append', index=False)

for year in years:
    print(year)
    seasonData = pandas.read_csv('./process/bundesliga-'+ year +'-table.csv')
    seasonData.to_sql('bundesliga_' + year+ '_table', conn, if_exists='append', index=False)
for year in years:
    print(year)
    seasonData = pandas.read_csv('./process/ligue1-'+ year +'-table.csv')
    seasonData.to_sql('ligue1_' + year+ '_table', conn, if_exists='append', index=False)

for year in years:
    print(year)
    seasonData = pandas.read_csv('./process/premierleague-'+ year +'-table.csv')
    seasonData.to_sql('premierleague_' + year+ '_table', conn, if_exists='append', index=False)

for year in years:
    print(year)
    seasonData = pandas.read_csv('./process/seriea-'+ year +'-table.csv')
    seasonData.to_sql('seriea_'+ year+ '_table', conn, if_exists='append', index=False)
print('ok')