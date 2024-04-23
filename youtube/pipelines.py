# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from typing import Optional
from youtube.items import YoutubeItem
from pydantic import BaseModel
from prisma import Prisma


class URLData(BaseModel):
    url: str
    title: str


class YoutubePipeline:
    def __init__(self):
        self.client = Prisma()
        self.client.connect()
        pass

    def __del__(self):
        self.client.disconnect()
        pass

    def remove_quotes(self, s):
        if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
            return s[1:-1]
        return s

    def process_item(self, item, spider):
        if type(item) != YoutubeItem:
            return item

        # print(item)
        # return item
        print(item)
        key = self.remove_quotes(item['href'])
        value = self.remove_quotes(item['title'])
        dto = URLData(url=key, title=value)
        print(dto)
        exists = self.client.url.count(
            where={
                'url': key
            }
        )
        print('count=', exists)
        if exists is False:
            print('not exists')
            res = self.client.url.create(data=dto.model_dump(exclude_none=True))
            print('res:', res)
        else:
            print('exists')

        return item


if __name__ == "__main__":
    try:
        client = Prisma()
        client.connect()
        dto = URLData(url='test1', title='title1')
        print(dto)
        res = client.url.create(data=dto.model_dump(exclude_none=True))
        print(res)
    except Exception as e:
        print(e)
    finally:
        client.disconnect()
        print("aaa")
