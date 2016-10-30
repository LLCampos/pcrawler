import scrapy


class SapoMagCrawler(scrapy.Spider):
    name = 'sapomag'
    start_urls = ['http://mag.sapo.pt/passatempos']

    def parse(self, response):

        passatempos_query = '//li[@class="tiny-100 small-50 medium-33 large-33 xlarge-33"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('div[2]/h4/text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
