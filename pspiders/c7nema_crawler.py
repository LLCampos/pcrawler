import scrapy


class C7nemaCrawler(scrapy.Spider):
    name = 'c7nema'
    start_urls = ['http://www.c7nema.net/passatempos2014.html']

    domain = 'http://www.c7nema.net'

    def parse(self, response):

        passatempos_query = '//ul[@id="b2j_k2_news_slider_ul_661"]/li/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = C7nemaCrawler.domain + \
                passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
