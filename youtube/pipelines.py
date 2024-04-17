# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from youtube.items import YoutubeItem
from upstash_redis import Redis

KV_REST_API_URL = "https://joint-guinea-50764.upstash.io"
KV_REST_API_TOKEN = "AcZMASQgNGUyYjhiZGYtOGU5Yi00MjQ2LWJjOTQtZGU0YjEwNTEyYjRkOWY5NmE0OTdhNzE3NGE3YThlMTA4Yjg2ODFlYTVhMTI="


class YoutubePipeline:
    def __init__(self):
        self.redis = Redis(url=KV_REST_API_URL, token=KV_REST_API_TOKEN)

    def process_item(self, item, spider):
        if type(item) != YoutubeItem:
            return item
        self.redis.set(item['href'], item['title'])
        return item


if __name__ == "__main__":
    redis = Redis(url=KV_REST_API_URL, token=KV_REST_API_TOKEN)
    redis.set("a", "b")
    print(redis.get("a"))
