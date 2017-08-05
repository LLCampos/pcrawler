import scrapy


class MTVCrawler(scrapy.Spider):
    name = 'mtv'
    start_urls = ['http://mtv.pt/passatempos/']

    domain = 'http://mtv.pt'

    def parse(self, response):

        passatempos_query = '//div[@class="tilesContainer case-4 params-active"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('div[@class="text"]/h4/text()').extract_first()

            # href is this page is relative, so I need to add the domain
            passatempo_url = MTVCrawler.domain + \
                passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
