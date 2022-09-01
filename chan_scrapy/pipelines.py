# See Documentation: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ChanScrapyPipeline(object):
    def process_item(self, item, spider):
        return item
