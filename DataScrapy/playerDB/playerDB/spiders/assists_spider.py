import scrapy
import playerDB.LinkGenerator as LinkGenerator
import csv
import re
import sys

class AssistsSpider(scrapy.Spider):
    name = "assists"
   
    def start_requests(self):
        # urls  = (LinkGenerator.generate_assists_links('Ligue-1'))
        # urls.extend(LinkGenerator.generate_assists_links('SerieA'))
        # urls.extend(LinkGenerator.generate_assists_links('LaLiga'))
        # urls.extend(LinkGenerator.generate_assists_links('Bundesliga'))
        # urls.extend(LinkGenerator.generate_assists_links('PrimerLeague'))
        urls = []
        urls.append('https://www.worldfootball.net/assists/esp-primera-division-2016-2017_2/')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        link_group = response.url.split("/")
        data_name = link_group[-2] + '-' + link_group[-3]
        assists_trs = response.css('table.standard_tabelle tr')
        filename = data_name + '.csv'
        with open(filename, 'w', encoding = 'utf-8') as f:
            csv_writer = csv.writer(f, delimiter=',' ,lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['player', 'country', 'team', 'assists'])
            for row in assists_trs[1:]:
                tds = row.css('td')
                name = tds[1].css('a::text').extract()
                country = tds[3].css('td::text').extract()
                team = tds[4].css('a')[1].css('a::text').extract()
                assists = tds[5].css('b::text').extract()
                
                csv_writer.writerow([str(name[0]), str(country[0]), str(team[0]), int(assists[0])])