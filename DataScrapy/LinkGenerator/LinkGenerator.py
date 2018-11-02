
base_url = 'https://www.worldfootball.net/%s/%s-%s/ '
LeagueDir = {'PrimerLeague':'eng-premier-league', 'Ligue-1':'fra-ligue-1',
              'SerieA':'ita-serie-a', 'LaLiga':'eng-premier-league',
              'Bundesliga':'bundesliga'}
YearList = ['2010-2011', '2011-2012', '2012-2013', '2013-2014', 
            '2014-2015', '2015-2016', '2016-2017', '2017-2018']

TableLists = ['goalgetter', 'assists', 'scorer']          


def main():
    for year in YearList:
        for table in TableLists:
            print(generate_link(table, 'PrimerLeague', year))
        print('-----------------------')

def generate_link(table, League, year):
    crawled_url = base_url%(table, LeagueDir[League], year)
    return crawled_url


if __name__ == '__main__':
    main()