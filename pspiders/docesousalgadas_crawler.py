import scrapy
from lxml import etree


class DocesOuSalgadasCrawler(scrapy.Spider):
    name = 'docesousalgadas'
    start_urls = ['http://docesousalgadas.pt/category/passatempos/']

    def parse(self, response):

        passatempos_query = '//h2[@class="entry-title"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }

