# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["http://www.quotes.toscrape.com/page/1"]

    def parse(self, response):
        self.log("I just visisted: " + response.url)

        yield {
            "author_name" : response.css(".author::text").extract_first(),
            "text" : response.css(".text::text").extract_first(),
            "tags" : response.css(".tag::text").extract()
	 } 