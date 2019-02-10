import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from Watcher.items import Formato7Item
from scrapy.exceptions import CloseSpider
from bs4 import BeautifulSoup


class Formato7Spider(CrawlSpider):
    name = 'formato7'
    item_count = 0
    allowed_domain = ['formato7.com']
    start_urls = ['https://formato7.com/category/noticias-de-veracruz/']

    rules = {
        Rule(LinkExtractor(
            allow=(), restrict_xpaths=('//a[@class="nextpostslink"]')
        )),
        Rule(LinkExtractor(
                allow=(), restrict_xpaths=('//h2[@class="entry-title"]')
            ),
            callback='parse_item',
            follow=False
        ),
    }

    def parse_item(self, response):
        item = Formato7Item()

        item['link'] = response.url

        item['title'] = response.xpath(
            '//*[@id="contenido"]/div/div/main/article/header/h1/text()'
        ).get('data')

        item['date'] = response.xpath(
            '//*[@id="contenido"]/div/div/main/article/header/div[2]/time/text()'
        ).get('data')

        item['cover_img'] = response.xpath(
            '//*[@id="contenido"]/div/div/main/article/header/div[1]/div[1]/img'
        ).attrib['src']

        elements = response.xpath(
            '//div[@class="articleBody"]/p[not(@class="sinetiks-anuncios")]'
        ).getall()

        item['body'] = ""
        for element in elements:
            node = BeautifulSoup(element, 'html.parser')
            for string in node.p.strings:
                item['body'] += string

        self.item_count += 1
        if self.item_count > 20:
            raise CloseSpider('item_exceeded')
        yield item
