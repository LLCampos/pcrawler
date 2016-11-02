import scrapy


class CinecartazCrawler(scrapy.Spider):
    name = 'cinecartaz'
    start_urls = ['http://cinecartaz.publico.pt/Passatempos']

    domain = 'http://cinecartaz.publico.pt'

    def parse(self, response):

        passatempos_query = '//ul[@class="itemindex resultadospesquisa basicvertlist stripelist"]/li'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('ul/li/h3/text()').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = CinecartazCrawler.domain + \
                passatempo.xpath('a/@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
