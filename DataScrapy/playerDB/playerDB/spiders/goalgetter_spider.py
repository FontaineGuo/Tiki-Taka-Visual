import scrapy
import LinkGenerator
import csv

class GoalGetterSpider(scrapy.Spider):
    name = "goalgetter"
   
    def start_requests(self):
        # for League in LinkGenerator.LeagueDir.keys():
        #     urls = LinkGenerator.generate_goalgetter_links(League)
        urls = []
        urls.append(LinkGenerator.generate_goalgetter_year_link('PrimerLeague', '2010'))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data_name = response.xpath('//*[@id="navi"]/div[3]/h1/text()').extract_first()
        goalgetter_table = response.xpath('//*[@id="site"]/div[3]/div[1]/div/div[3]/div/table/')
        rows = goalgetter_table.xpath('//tr')
        filename = data_name + '.csv'
        with open(filename, 'wb') as f:
            fwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            # write title
            fwriter