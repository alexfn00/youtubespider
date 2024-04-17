from pprint import pprint

import scrapy
from selenium import webdriver

from youtube.items import YoutubeItem


class YtSpider(scrapy.Spider):
    name = "yt"
    allowed_domains = ["youtube.com"]
    start_urls = ["https://www.youtube.com/@BroCodez/video"]
    models_urls = []

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def closed(self, spider):
        self.driver.quit()

    def parse(self, response):
        selectors = response.xpath('//*[@id="contents"]')
        for selector in selectors:
            videos = selector.xpath('//a[@id="video-title"]')
            for video in videos:
                item = YoutubeItem()
                item['title'] = video.xpath('./@title').extract_first()
                item['href'] = video.xpath('./@href').extract_first()
                yield item
