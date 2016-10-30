import scrapy


class TransportesLisboaCrawler(scrapy.Spider):
    name = 'transporteslisboa'
    start_urls = ['http://passatempos.transporteslisboa.pt/']

    def parse(self, response):

        passatempos_query = '//h1[@class="entry-title"]/a '

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
