import scrapy


class CaixaIUCrawler(scrapy.Spider):
    name = 'caixaiu'
    start_urls = ['http://www.caixaiu.pt/actualidade/passatempos/']

    def parse(self, response):

        passatempos_query = '//h1[@class="post-title"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
