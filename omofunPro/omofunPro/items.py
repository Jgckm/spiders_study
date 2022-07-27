# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OmofunproItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image_url = scrapy.Field()
    status = scrapy.Field()
    detail = scrapy.Field()
    id = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    type = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    update = scrapy.Field()
    player = scrapy.Field()