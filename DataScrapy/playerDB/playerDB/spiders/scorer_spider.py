import scrapy
#import module.LinkGenerator as LinkGenerator
class ScorerSpider(scrapy.Spider):
    name = "scorer"
   
    def start_requests(self):
        # for League in LinkGenerator.LeagueDir.keys():
        #     urls = LinkGenerator.generate_scorer_links(League)
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)
        pass

    def parse(self, response):
        pass