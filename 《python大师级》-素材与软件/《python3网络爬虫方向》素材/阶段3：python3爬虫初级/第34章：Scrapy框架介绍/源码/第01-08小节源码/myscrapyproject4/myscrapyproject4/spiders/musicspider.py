# -*- coding: utf-8 -*-
import scrapy
from lxml import etree


class MusicspiderSpider(scrapy.Spider):
    name = 'musicspider'
    allowed_domains = ['htqyy.com/']
    start_urls = ['http://www.htqyy.com/']

    def parse(self, response):

        res_list = response.xpath("//a[@class='song']/@title")
        for i in res_list:
            res_value = {}
            res_value["title"] = i.get()
            yield res_value
         
