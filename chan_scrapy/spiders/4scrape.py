# -*- coding: utf-8 -*-
import scrapy


class ChanCrawler(scrapy.Spider):
    name = "chanCrawler"
    start_urls = ["http://www.4chan.org/a/"]

    def parse(self, response):
        self.log("I just visisted: " + response.url)

        subjects = response.css(".subject::text").extract()

        for item in zip(subjects):
            scraped_info = {
                'subject' : item[0]
            }

            yield scraped_info
