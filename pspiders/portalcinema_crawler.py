import scrapy


class PortalCinemaCrawler(scrapy.Spider):
    name = 'portalcinema'
    start_urls = ['http://www.portal-cinema.com/search/label/Passatempo']

    def parse(self, response):

        passatempos_query = '//h3[@class="post-title entry-title"]/a'

        for passatempo in response.xpath(passatempos_query):
            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
