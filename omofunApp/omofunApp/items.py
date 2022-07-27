# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OmofunappItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    images = scrapy.Field()
    update = scrapy.Field()
    remarks = scrapy.Field()
    type = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()
    blurb = scrapy.Field()
    score = scrapy.Field()
    actor = scrapy.Field()
    year = scrapy.Field()
    lang = scrapy.Field()
    player_list = scrapy.Field()
