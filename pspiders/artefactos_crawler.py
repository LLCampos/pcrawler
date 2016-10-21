import scrapy


class ArteFactosCrawler(scrapy.Spider):
    name = 'artefactos'
    start_urls = ['http://www.arte-factos.net/passatempos-af/']

    def parse(self, response):
        for passatempo in response.xpath('//div[@class="titulo-pagina"]/a'):
            yield {
                passatempo.xpath('h4/text()').extract_first(): passatempo.xpath('@href').extract_first()
            }
