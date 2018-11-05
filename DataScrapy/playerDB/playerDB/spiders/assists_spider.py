import scrapy
import LinkGenerator

class AssistsSpider(scrapy.Spider):
    name = "assists"
   
    def start_requests(self):
        urls = [
            'https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/2458/England-Premier-League'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'topplayer.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)