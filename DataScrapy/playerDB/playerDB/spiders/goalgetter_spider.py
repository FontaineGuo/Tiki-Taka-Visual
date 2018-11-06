import scrapy
import playerDB.LinkGenerator as LinkGenerator
import csv
import re
import sys

class GoalGetterSpider(scrapy.Spider):
    name = "goalgetter"
    
    def start_requests(self):
        # urls  = (LinkGenerator.generate_goalgetter_links('Ligue-1'))
        # urls.extend(LinkGenerator.generate_goalgetter_links('SerieA'))
        # urls.extend(LinkGenerator.generate_goalgetter_links('LaLiga'))
        # urls.extend(LinkGenerator.generate_goalgetter_links('Bundesliga'))
        urls = []
        urls.append('https://www.worldfootball.net/goalgetter/esp-primera-division-2016-2017_2/')
        # urls.append('https://www.worldfootball.net/goalgetter/eng-premier-league-2010-2011/')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        link_group = response.url.split("/")
        data_name = link_group[-2] + '-' + link_group[-3]
        goalgetter_trs = response.css('table.standard_tabelle tr')
        filename = data_name + '.csv'
        with open(filename, 'w', encoding = 'utf-8') as f:
            csv_writer = csv.writer(f, delimiter=',' ,lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
            pattern = r'\((\d{0,2})\)'
            # write title
            csv_writer.writerow(['player', 'country', 'team', 'goal', 'penalty'])
            for row in goalgetter_trs[1:]:
                tds = row.css('td')
                name = tds[1].css('a::text').extract()
                country = tds[3].css('td::text').extract()
                team = tds[4].css('a')[1].css('a::text').extract()
                goals = tds[5].css('b::text').extract()
                penalty = re.search(pattern, str(tds[5].css('td::text').extract()))[1]

                csv_writer.writerow([str(name[0]), str(country[0]), str(team[0]), int(goals[0]), int(penalty)])