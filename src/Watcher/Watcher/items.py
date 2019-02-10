# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Formato7Item(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    body = scrapy.Field()
    actors = scrapy.Field()
    place = scrapy.Field()
    cover_img = scrapy.Field()
    link = scrapy.Field()
