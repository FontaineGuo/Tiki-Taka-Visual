import scrapy
import playerDB.LinkGenerator as LinkGenerator
import csv
import re
import sys

class GoalGetterSpider(scrapy.Spider):
    name = "goalgetter"
    
    def start_requests(self):

       
        urls = []
        urls.append(LinkGenerator.generate_goalgetter_year_link('PrimerLeague', '2010'))
        # urls.append('https://www.worldfootball.net/goalgetter/eng-premier-league-2010-2011/')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data_name = response.xpath('//*[@id="navi"]/div[3]/h1/text()').extract_first()
        goalgetter_trs = response.xpath('table.standard_tabelle tr')
        filename = data_name + '.csv'
        with open(filename, 'wb') as f:
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
                penalty = re.search(pattern, tds[5].css('td::text').extract())[1]

                csv_writer.writerow([name, country, team, int(goals), int(penalty)])