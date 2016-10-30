import scrapy


class MaximaCrawler(scrapy.Spider):
    name = 'maxima'
    start_urls = ['http://www.maxima.pt/passatempos.html']

    domain = 'http://www.maxima.pt'

    def parse(self, response):

        passatempos_query = '//div[@class="canal_subdestaqueInfo"]/a[2]'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = MaximaCrawler.domain + \
                passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
