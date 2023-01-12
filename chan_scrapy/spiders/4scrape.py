# -*- coding: utf-8 -*-
import scrapy
import logging
from ..items import ChanImageItem

board = "a/"

class ChanCrawler(scrapy.Spider):
    name = "chanCrawler"
    start_urls = ["http://boards.4channel.org/"+ board]

    #init for setting the board to access
    def __init__(self, start_url=None, *args, **kwargs):
        super(ChanCrawler, self).__init__(*args, **kwargs)
        self.start_url = "https://boards.4channel.org/" + start_url + "/"

    #parsing entire board, iterating pages on it
    def parse(self, response):
        self.log("THE START URL IS: " + self.start_url)
        #prints if the crawler is started correctly
        self.log("I just visisted: " + response.url)
        
        #first page is run seperately as "4channel.org/a/1" does not return a valid site
        yield scrapy.Request(url=self.start_url, callback=self.parse_page)

        #remaining pages are parsed
        page = 1
        while(page < 10):
            page += 1
            yield scrapy.Request(url=self.start_url + str(page), callback=self.parse_page)

    #page is parsed
    def parse_page(self, response):

        for thread in response.css("span.summary.desktop .replylink"):
            yield scrapy.Request(url=self.start_url + thread.css("a::attr(href)").extract_first(), callback=self.parse_thread)

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
