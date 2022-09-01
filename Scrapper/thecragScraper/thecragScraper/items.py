# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ThecragscraperItem(scrapy.Item):
    name = scrapy.Field()
    grade = scrapy.Field()
    tags = scrapy.Field()
    description = scrapy.Field()
