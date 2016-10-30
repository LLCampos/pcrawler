import scrapy


class MagazineHDCrawler(scrapy.Spider):
    name = 'magazinehd'
    start_urls = ['http://www.magazine-hd.com/apps/wp/category/passatempos/passatempos-a-decorrer']

    def parse(self, response):

        passatempos_query = '//h3[@class="entry-title"]/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
