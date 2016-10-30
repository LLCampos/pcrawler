import scrapy


class LuxWomanCrawler(scrapy.Spider):
    name = 'luxwoman'
    start_urls = ['http://www.luxwoman.pt/passatempo/']

    def parse(self, response):

        passatempos_query = '//li[@class="infinite-post"]/div[2]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
