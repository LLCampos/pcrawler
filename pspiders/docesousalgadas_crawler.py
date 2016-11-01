import scrapy
from lxml import etree


class DocesOuSalgadasCrawler(scrapy.Spider):
    '''Here I scrap the RSS feed. It's easier because the site is based on
    Javascript.'''
    name = 'docesousalgadas'
    start_urls = ['https://docesousalgadas.blogspot.pt//feeds/posts/default']

    def parse(self, response):

        namespace = 'http://www.w3.org/2005/Atom'
        tree = etree.fromstring(response.text.encode('utf-8'))

        passatempos_query = 'x:entry[x:title[contains(text(), "Passatempo")]]'
        passatempos = tree.xpath(passatempos_query, namespaces={'x': namespace})

        for passatempo in passatempos:

            passatempo_name = passatempo.xpath('x:title/text()', namespaces={'x': namespace})[0]
            passatempo_url = passatempo.xpath('x:link[@rel="alternate"]/@href', namespaces={'x': namespace})[0]

            yield {
                "name": passatempo_name,
                "url": passatempo_url
            }
