# -*- coding: utf-8 -*-
import scrapy
from ..items import ChanImageItem

class ChanCrawler(scrapy.Spider):
    name = "chanCrawler"
    start_urls = ["http://boards.4channel.org/a/"]

    def parse(self, response):
        #prints if the crawler is started correctly
        self.log("I just visisted: " + response.url)
        
        #first page is run seperately as "4channel.org/a/1" does not return a valid site
        yield scrapy.Request(url="http://boards.4channel.org/a/", callback=self.parse_page)

        page = 1
        while(page < 10):
            page += 1
            yield scrapy.Request(url="http://boards.4channel.org/a/" + str(page), callback=self.parse_page)

    def parse_page(self, response):

        for thread in response.css("span.summary.desktop .replylink"):
            yield scrapy.Request(url="http://boards.4channel.org/a/" + thread.css("a::attr(href)").extract_first(), callback=self.parse_thread)

    def parse_thread(self, response):        
        item = ChanImageItem()
        fil_urls = []

        for fil in response.css(".fileThumb"):
            fil_urls.append("http:" + fil.css("a::attr(href)").extract_first())
        item["file_urls"] = fil_urls
        return item
