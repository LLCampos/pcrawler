import scrapy


class CinemundoCrawler(scrapy.Spider):
    name = 'cinemundo'
    start_urls = ['http://www.cinemundo.pt/passatempos/']

    def parse(self, response):

        passatempos_query = '//div[@class="col-md-6 text-normal element-top-0 element-bottom-20 text-center"]//a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
