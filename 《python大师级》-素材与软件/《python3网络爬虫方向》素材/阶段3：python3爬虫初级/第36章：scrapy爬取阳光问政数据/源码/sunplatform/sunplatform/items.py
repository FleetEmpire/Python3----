# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunplatformItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Scrapy.Field类就是内置dict类的一个子类
    # 每个帖子的标题，相当于创建了字典，title是字典名称
    title = scrapy.Field()
    # 每个帖子的内容
    content_ask = scrapy.Field()
    # 每个帖子的url
    content_answer = scrapy.Field()

    pass
