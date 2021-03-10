# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChanScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ChanImageItem(scrapy.Item):
    files = scrapy.Field()
    file_urls = scrapy.Field()
