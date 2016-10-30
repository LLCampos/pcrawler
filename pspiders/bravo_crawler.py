import scrapy


class BravoCrawler(scrapy.Spider):
    name = 'bravo'
    start_urls = ['http://www.bravo.pt/categoria/passatempos/']

    def parse(self, response):

        passatempos_query = '//h2[@class="cb-post-title"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
