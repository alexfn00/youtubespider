from pprint import pprint

import scrapy
from selenium import webdriver


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
            items = selector.xpath('//a[@id="video-title"]')
            for item in items:
                print(item.xpath('./@href').extract_first(), item.xpath('./@title').extract_first())

