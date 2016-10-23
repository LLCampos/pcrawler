import scrapy


class RitmosBlues(scrapy.Spider):
    name = 'ritmos_e_blues'
    start_urls = ['http://www.ritmoseblues.pt/passatempos/']

    domain = 'http://www.ritmoseblues.pt'

    def parse(self, response):

        passatempos_query = '//div[@class="center-wraper"]/table'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('.//span[@class="event-sub-tituloW"]/text()').extract_first()
            # href is this page is relative, so I need to add the domain
            # also, the href in this page is like this: ../bieber/passatempo/",
            # so I take off the two points
            passatempo_url = RitmosBlues.domain + \
                passatempo.xpath('.//table//a/@href').extract_first()[2:]

            yield {
                "passatempo_name": passatempo_name,
                "passatempo_url": passatempo_url
            }
