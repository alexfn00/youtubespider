from pprint import pprint
from time import sleep

import scrapy
from selenium import webdriver
from pprint import pprint

from youtube.items import YoutubeItem


class YtSpider(scrapy.Spider):
    name = "yt"
    allowed_domains = ["youtube.com"]
    start_urls = None
    author = None
    url = 'https://www.youtube.com/@'
    # start_urls = ["https://www.youtube.com/@BroCodez/video"]
    models_urls = []

    def __init__(self, author='', *args, **kwargs):
        super(YtSpider, self).__init__(*args, **kwargs)
        self.author = author
        start_url = self.url + author
        print(start_url)
        self.start_urls = [start_url]
        # self.start_urls = ['https://www.youtube.com/@BroCodez/videos']
        print(self.start_urls)
        options = webdriver.FirefoxOptions()
        proxy = "127.0.0.1:7890"
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--disable-extensions')
        # options.add_experimental_option('excludeSwitches',['ignore-certificate-errors'])
        # options.add_argument('--start-maximized')

        # options.add_argument('--proxy-server=%s' % proxy)
        options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Firefox(options=options)
        # pass

    def closed(self, spider):
        self.driver.quit()
        pass

    def parse(self, response):
        avatar = response.xpath('//*[@id="avatar"]').xpath('./img/@src').extract_first()
        print(avatar)
        
        selectors = response.xpath('//*[@id="inner-header-container"]')
        # print(selectors)
        print('****************************************')
        
        
        for selector in selectors:
            result = selector.xpath('//*[@id="text"]')
            # print(result)
            title = result.xpath('./text()').extract_first()
            print(title)

        # url = self.url + self.author+ '/videos'
        url = 'https://www.youtube.com/@BroCodez/videos'
        sleep(1)
        yield scrapy.Request(url=url, callback=self.parse_video)

    def parse_video(self, response):
        # meta = response.meta
        print('parse_video')
        # print(response)
        selectors = response.xpath('//*[@id="contents"]')
        # print(selectors)
        for selector in selectors:
            print('selector')
            videos = selector.xpath('//a[@id="video-title"]')
            print(videos)
            for video in videos:
                item = YoutubeItem()
                item['author'] = 'meta'
                item['title'] = video.xpath('./@title').extract_first()
                item['href'] = video.xpath('./@href').extract_first()
                print(item)
                # yield item
