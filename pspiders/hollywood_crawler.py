import scrapy


class HollywoodCrawler(scrapy.Spider):
    name = 'hollywood'
    start_urls = ['http://canalhollywood.pt/passatempos/']

    domain = 'http://canalhollywood.pt'

    def parse(self, response):
        for passatempo in response.xpath('//div[contains(@class, "entrada-blog")]'):
            yield {
                # href is this page is relative, so I need to add the domain
                passatempo.xpath('div/h2/text()').extract_first(): HollywoodCrawler.domain + passatempo.xpath('div/a/@href').extract_first()
            }
