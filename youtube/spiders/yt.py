from pprint import pprint

import scrapy
from selenium import webdriver

from youtube.items import YoutubeItem


class YtSpider(scrapy.Spider):
    name = "yt"
    allowed_domains = ["youtube.com"]
    # start_urls = ["https://www.youtube.com/@BroCodez/video"]
    models_urls = []

    def __init__(self,  author='', *args, **kwargs):
        super(YtSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.youtube.com/@'.join(author)]


        options = webdriver.ChromeOptions()
        proxy = "127.0.0.1:7890"
        options.add_argument('--proxy-server=%s' % proxy)
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def closed(self, spider):
        self.driver.quit()

    def parse(self, response):
        selectors = response.xpath('//*[@id="page-header"]')
        print(selectors)

    def parse_video(self, response):
        selectors = response.xpath('//*[@id="contents"]')
        for selector in selectors:
            videos = selector.xpath('//a[@id="video-title"]')
            for video in videos:
                item = YoutubeItem()
                item['title'] = video.xpath('./@title').extract_first()
                item['href'] = video.xpath('./@href').extract_first()
                yield item
