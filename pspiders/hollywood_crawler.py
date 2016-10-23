import scrapy


class HollywoodCrawler(scrapy.Spider):
    name = 'hollywood'
    start_urls = ['http://canalhollywood.pt/passatempos/']

    domain = 'http://canalhollywood.pt'

    def parse(self, response):

        passatempos_query = '//div[contains(@class, "entrada-blog")]'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('div/h2/text()').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = HollywoodCrawler.domain + \
                passatempo.xpath('div/a/@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
