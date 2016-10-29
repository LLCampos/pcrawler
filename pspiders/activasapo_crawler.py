import scrapy


class ActivaSapoCrawler(scrapy.Spider):
    name = 'activa sapo'
    start_urls = ['http://activa.sapo.pt/passatempos/']

    domain = 'http://activa.sapo.pt'

    def parse(self, response):

        passatempos_query = '//div[@class="textDetails"]/h2[@class="title"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = ActivaSapoCrawler.domain + \
                passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
