import scrapy


class CinemasNOSCrawer(scrapy.Spider):
    name = 'cinemas_nos'
    start_urls = ['http://cinemas.nos.pt/passatempos/']

    def parse(self, response):

        passatempos_query = '//div[@id="WebPartWPQ3"]/table/tr/td[1]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
