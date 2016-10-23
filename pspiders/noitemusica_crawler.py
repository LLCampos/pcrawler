import scrapy


class NoiteMusicaMagazineCrawer(scrapy.Spider):
    name = 'noite_musica_magazine'
    start_urls = ['http://www.noitemusicamagazine.pt/category/passatempos']

    def parse(self, response):

        passatempos_query = '//div[@class="postarea"]/h1/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
