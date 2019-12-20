import scrapy
from ..items import ChanImageItem


class ChanCrawler(scrapy.Spider):
    name = "testCrawler"
    start_urls = ["http://boards.4channel.org/a/"]

    def parse(self, response):
        self.log("I just visisted: " + response.url)
        
        for thread in response.css("span.summary.desktop .replylink"):
            yield scrapy.Request(url="http://boards.4channel.org/a/" + thread.css("a::attr(href)").extract_first(), callback=self.parse_thread)

    def parse_thread(self, response):
        item = ChanImageItem()
        fil_urls = []

        for fil in response.css(".fileThumb"):
            fil_urls.append("http:" + fil.css("a::attr(href)").extract_first())
        item["file_urls"] = fil_urls
        return item

