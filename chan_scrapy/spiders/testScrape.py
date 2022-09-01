import scrapy
from ..items import ChanImageItem
from ..trans import has_transparency
import logging
import requests
import io
from PIL import Image


class ChanCrawler(scrapy.Spider):
    name = "testCrawler"
    start_urls = ["http://boards.4channel.org/a/"]

    def parse(self, response):
        self.log("I just visisted: " + response.url)
        
        #scrape only first thread
        #thread = response.css("span.summary.desktop .replylink")[0]
        #yield scrapy.Request(url="http://boards.4channel.org/a/" + thread.css("a::attr(href)").extract_first(), callback=self.parse_thread)

        #scrape all threads on first page
        for thread in response.css("span.summary.desktop .replylink"):
            yield scrapy.Request(url="http://boards.4channel.org/a/" + thread.css("a::attr(href)").extract_first(), callback=self.parse_thread)

    def parse_thread(self, response):
        item = ChanImageItem()
        fil_urls = []
        trans_urls = []

        for fil in response.css(".fileThumb"):
            fil_urls.append("http:" + fil.css("a::attr(href)").extract_first())

        #Attempt to download image to memory as opposed to disk
        for image in fil_urls:
            data = requests.get(image).content
            data_bytes = io.BytesIO(data)
            img = Image.open(data_bytes)
            if(has_transparency(img)):
                trans_urls.append(image)

        item["file_urls"] = trans_urls
        return item

