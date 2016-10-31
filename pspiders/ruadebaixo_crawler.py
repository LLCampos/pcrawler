import scrapy


class RuaDeBaixoCrawler(scrapy.Spider):
    name = 'ruadebaixo'
    start_urls = ['http://www.ruadebaixo.com/passatempos']

    def parse(self, response):

        passatempos_query = '//div[@class="article__title  article--thumb__title"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('h3/text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
