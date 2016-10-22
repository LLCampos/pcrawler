import scrapy


class EcrawlerCrawer(scrapy.Spider):
    name = 'e-crawler'
    start_urls = ['http://www.e-cultura.sapo.pt/']

    def parse(self, response):

        passatempos_query = '//div[@class="side_passatempo"]'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('.//a/text()')[-1].extract()
            passatempo_link = passatempo.xpath('.//a/@href').extract_first()

            yield {
                passatempo_name: passatempo_link
            }
