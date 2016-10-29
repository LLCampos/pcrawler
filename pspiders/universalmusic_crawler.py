import scrapy


class UniversalMusicCrawler(scrapy.Spider):
    name = 'universal music'
    start_urls = ['http://www.universalmusic.pt/passatempo']

    domain = 'http://www.universalmusic.pt'

    def parse(self, response):

        passatempos_query = '//div[@class="row passatempos"]/div[@class="col-md-4 col-sm-4"]'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('h3/text()').extract_first()
            # href is this page is relative, so I need to add the domain
            passatempo_url = UniversalMusicCrawler.domain + \
                passatempo.xpath('a/@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
