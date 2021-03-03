# -*- coding: utf-8 -*-
import scrapy
import logging
from ..items import ChanImageItem

class ChanCrawler(scrapy.Spider):
    name = "chanCrawler"
    start_urls = ["http://boards.4channel.org/a/"]

    #parsing entire board, iterating pages on it
    def parse(self, response):
        #prints if the crawler is started correctly
        self.log("I just visisted: " + response.url)
        
        #first page is run seperately as "4channel.org/a/1" does not return a valid site
        yield scrapy.Request(url="http://boards.4channel.org/a/", callback=self.parse_page)

        #remaining pages are parsed
        page = 1
        while(page < 10):
            page += 1
            yield scrapy.Request(url="http://boards.4channel.org/a/" + str(page), callback=self.parse_page)

    #page is parsed
    def parse_page(self, response):

        for thread in response.css("span.summary.desktop .replylink"):
            yield scrapy.Request(url="http://boards.4channel.org/a/" + thread.css("a::attr(href)").extract_first(), callback=self.parse_thread)

    #thread on page is parsed
    def parse_thread(self, response):        
        item = ChanImageItem()
        fil_urls = []
        ext = [".png", ".webm", ".gif"]

        for fil in response.css(".fileThumb"):
            #save response as a string so we can check extensions
            picstring = str(fil.css("a::attr(href)").extract_first)
            
            logging.debug("Response looks like: " + picstring + " does it end with designed?: " + str(picstring.endswith(tuple(ext), 0, len(picstring)-4)))
            if(picstring.endswith(tuple(ext), 0, len(picstring)-4)):
                fil_urls.append("http:" + fil.css("a::attr(href)").extract_first())
        item["file_urls"] = fil_urls
        return item
