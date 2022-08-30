# -*- coding: utf-8 -*-
import scrapy

class MusicspiderSpider(scrapy.Spider):
    name = 'musicspider'
    allowed_domains = ['htqyy.com']
    start_urls = ['http://www.htqyy.com/genre/1']

    def parse(self, response):
        title_list = response.xpath("//li[@class='mItem']//span[@class='title']//a//@title")
        artist_name_list = response.xpath("//li[@class='mItem']//span[@class='artistName']//a//@title")
        album_name_list = response.xpath("//li[@class='mItem']//span[@class='albumName']//a//@title")
        play_count_list = response.xpath("//li[@class='mItem']//span[@class='playCount']")
        item_value = {}
        item_value["title_list"] = title_list
        item_value["artist_name_list"] = artist_name_list
        item_value["album_name_list"] = album_name_list
        item_value["play_count_list"] = play_count_list
        yield item_value
        #提取板块页码
        page = int(response.url[-1])+1
        if page <= 5:
            next_url = response.url[:-1] + str(page)
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse)



