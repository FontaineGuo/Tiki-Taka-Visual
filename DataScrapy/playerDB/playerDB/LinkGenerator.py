
import re

base_url = 'https://www.worldfootball.net/%s/%s-%s/ '
LeagueDir = {'PrimerLeague':'eng-premier-league', 'Ligue-1':'fra-ligue-1',
              'SerieA':'ita-serie-a', 'LaLiga':'eng-premier-league',
              'Bundesliga':'bundesliga'}


YearList = {'2010':'2010-2011', '2011':'2011-2012', '2012':'2012-2013', '2013':'2013-2014', 
            '2014':'2014-2015', '2015':'2015-2016', '2016':'2016-2017', '2017':'2017-2018'}

TableLists = ['goalgetter', 'assists', 'scorer']          


def main():
    # for year in YearList:
    #     for table in TableLists:
    #         print(generate_link(table, 'PrimerLeague', year))
    #     print('-----------------------')


    # urls = generate_goalgetter_links('PrimerLeague')
    # for url in urls:
    #     print(url)

    # urls = generate_assists_links('PrimerLeague')
    # for url in urls:
    #     print(url)

    # urls = generate_scorer_links('PrimerLeague')
    # for url in urls:
    #     print(url)
    pass
    

def generate_link(table, League, year):
    crawled_url = base_url%(table, LeagueDir[League], YearList[year])
    return crawled_url


# generate goalgetter links from 2010-2018
def generate_goalgetter_links(League):
    crawled_urls = []
    for year in YearList.values():
        crawled_urls.append(base_url%(TableLists[0], LeagueDir[League], year))
    return crawled_urls
# generate goalgetter link by year
def generate_goalgetter_year_link(League, year):
    return base_url%(TableLists[0], LeagueDir[League], YearList[year])

# generate assists links from 2010-2018
def generate_assists_links(League):
    crawled_urls = []
    for year in YearList.values():
        crawled_urls.append(base_url%(TableLists[1], LeagueDir[League], year))
    return crawled_urls

# generate assists year by link
def generate_assists_year_link(League, year):
    return base_url%(TableLists[1], LeagueDir[League], YearList[year])

# generate scorer links from 2010-2018
def generate_scorer_links(League):
    crawled_urls = []
    for year in YearList.values():
        crawled_urls.append(base_url%(TableLists[2], LeagueDir[League], year))
    return crawled_urls

# generatge scorer link by year
def generate_scorer_year_link(League, year):
    return base_url%(TableLists[2], LeagueDir[League], YearList[year])

if __name__ == '__main__':
    main()