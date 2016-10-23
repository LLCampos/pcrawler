import scrapy


class ArteFactosCrawler(scrapy.Spider):
    name = 'artefactos'
    start_urls = ['http://www.arte-factos.net/passatempos-af/']

    def parse(self, response):

        passatempos_query = '//div[@class="titulo-pagina"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('h4/text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
