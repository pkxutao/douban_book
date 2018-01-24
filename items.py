# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    imgUrl = scrapy.Field()
    author = scrapy.Field()
    name = scrapy.Field()
    press = scrapy.Field()
    score = scrapy.Field()
    pageCount = scrapy.Field()
    price = scrapy.Field()
    isbn = scrapy.Field()
    publishYear = scrapy.Field()
    binding = scrapy.Field()
    label = scrapy.Field()
