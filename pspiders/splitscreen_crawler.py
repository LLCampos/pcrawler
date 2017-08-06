import scrapy


class SplitscreenCrawler(scrapy.Spider):
    name = 'splitescreen'
    start_urls = ['http://splitscreen-blog.blogspot.pt/p/passatempos.html']

    def parse(self, response):

        passatempos_query = '//div[@class="post-body entry-content"]/div[2]/div[2]/div/a'


        for passatempo in response.xpath(passatempos_query):

            passatempo_url = passatempo.xpath('@href').extract_first()
            passatempo_name = passatempo_url.split('/')[-1]

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }