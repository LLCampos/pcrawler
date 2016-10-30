import scrapy


class CinemaMetropolisCrawler(scrapy.Spider):
    name = 'cinemametropolis'
    start_urls = ['http://cinemametropolis.com/index.php/pt/passatempos']

    domain = 'http://cinemametropolis.com'

    def parse(self, response):

        passatempos_query = '//div[@class="itemBlock"]//h2/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = CinemaMetropolisCrawler.domain + \
                passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
