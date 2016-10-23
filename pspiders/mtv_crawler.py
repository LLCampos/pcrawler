import scrapy


class MTVCrawler(scrapy.Spider):
    name = 'hollywood'
    start_urls = ['http://mtv.pt/passatempos/']

    domain = 'http://mtv.pt'

    def parse(self, response):

        passatempos_query = '//div[@data-mtv-module-shortid="nu7kqa"]/div//a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath("div/h3/span/text()").extract_first()

            # href is this page is relative, so I need to add the domain
            passatempo_url = MTVCrawler.domain + \
                passatempo.xpath('@href').extract_first()

            yield {
                "passatempo_name": passatempo_name,
                "passatempo_url": passatempo_url
            }
