import scrapy


class AXNCrawler(scrapy.Spider):
    name = 'axn'
    start_urls = ['http://www.axn.pt/contests']

    domain = 'http://www.axn.pt'

    def parse(self, response):

        passatempos_query = '//div[@class="promo-teaser snippet contest"]//h2/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = AXNCrawler.domain + \
                passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
