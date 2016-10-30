import scrapy


class Antena3Crawler(scrapy.Spider):
    name = 'antena3'
    start_urls = ['http://media.rtp.pt/antena3/passatempos/']

    def parse(self, response):

        passatempos_query = '//h3[@class="entry-title"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
