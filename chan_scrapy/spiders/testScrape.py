import scrapy


class ChanCrawler(scrapy.Spider):
    name = "testCrawler"
    start_urls = ["http://www.4chan.org/a/"]

    def parse(self, response):
        self.log("I just visisted: " + response.url)

        subjects = response.css(".subject::text").extract()
        postmsg = response.css(".postMessage::text").extract()

        for item in zip(subjects, postmsg):
            scraped_info = {
                'subject' : item[0],
                'postmsg' : item[1],
            }

            yield scraped_info