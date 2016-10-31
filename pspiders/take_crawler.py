import scrapy


class TakeCrawler(scrapy.Spider):
    name = 'take'
    start_urls = ['http://take.com.pt/passatempos/']

    def parse(self, response):

        passatempos_query = '//h3[@class="g1-beta g1-beta-1st entry-title"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
