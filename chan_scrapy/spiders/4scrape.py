# -*- coding: utf-8 -*-
import scrapy


class ChanCrawler(scrapy.Spider):
    name = "chanCrawler"
    start_urls = ["http://boards.4channel.org/a/"]

    def parse(self, response):
        self.log("I just visisted: " + response.url)
        
        #first page is run seperately as "4channel.org/a/1" does not return a valid site
        yield scrapy.Request(url="http://boards.4channel.org/a/", callback=self.parse_page)

        page = 1
        while(page < 10):
            page += 1
            yield scrapy.Request(url="http://boards.4channel.org/a/" + str(page), callback=self.parse_page)

    def parse_page(self, response):
        subjects = response.css(".subject::text").extract()

        for item in zip(subjects):
            scraped_info = {
                'subject' : item[0]
            }

            yield scraped_info
