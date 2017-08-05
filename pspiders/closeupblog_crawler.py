import scrapy


class CloseUpBlogCrawler(scrapy.Spider):
    name = 'closeupblog'
    start_urls = ['http://close-up-blog.blogspot.pt/p/passatempos-decorrer.html']

    def parse(self, response):

        passatempos_query = '//div[@class="post hentry"]//b/a'

        for passatempo in response.xpath(passatempos_query):

            passatempo_name = passatempo.xpath('span/text()').extract_first()
            passatempo_url = passatempo.xpath('@href').extract_first()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
