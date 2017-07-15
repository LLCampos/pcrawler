import scrapy


class RTPCinemaxCrawler(scrapy.Spider):
    name = 'rtpcinemax'
    start_urls = ['http://www.rtp.pt/cinemax/?headline=23']

    def parse(self, response):

        passatempos_query = '//ul/li/div/div[1]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('@title').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
