import scrapy


class CinemaCityCrawer(scrapy.Spider):
    name = 'cinemacity'
    start_urls = ['http://www.cinemacity.pt/editoriais/passatempos/']

    def parse(self, response):

        passatempos_query = '//div[@class="item"]//h3/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
