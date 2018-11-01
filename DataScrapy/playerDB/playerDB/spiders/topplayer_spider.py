import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/2458/England-Premier-League',
            'https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/3853/England-Premier-League',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)