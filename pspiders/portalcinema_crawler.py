import scrapy


class PortalCinemaCrawler(scrapy.Spider):
    name = 'portalcinema'
    start_urls = ['http://www.portal-cinema.com/']

    def parse(self, response):

        passatempo_query = '//a[text()="Passatempo"]'
        passatempo = response.xpath(passatempo_query)[0]

        passatempo_name = passatempo.xpath('text()').extract_first()
        passatempo_url = passatempo.xpath('@href').extract_first()

        yield {
            "name": passatempo_name,
            "url": passatempo_url
        }
