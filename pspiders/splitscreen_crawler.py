import scrapy


class SplitscreenCrawler(scrapy.Spider):
    name = 'splitescreen'
    start_urls = ['http://splitscreen-blog.blogspot.pt/p/passatempos.html']

    def parse(self, response):

        passatempos_query = '//div[@class="post-body entry-content"]/div[2]/div[2]/div'
        names = response.xpath(passatempos_query + '/b/text()')
        urls = response.xpath(passatempos_query + '/a/@href')

        if len(names) != len(urls):
            raise ValueError('There\'s something wrong '
                             'in the xpath expressions')

        for i in range(len(names)):

            passatempo_name = names[i].extract()
            passatempo_url = urls[i].extract()

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
