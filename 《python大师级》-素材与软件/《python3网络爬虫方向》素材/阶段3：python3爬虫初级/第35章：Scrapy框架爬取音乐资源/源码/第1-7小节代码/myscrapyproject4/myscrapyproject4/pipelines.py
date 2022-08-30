# -*- coding: utf-8 -*-
import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#管道文件，进行数据的处理和保存
class Myscrapyproject4Pipeline:

    def __init__(self): #定义一些需要初始化的方法
        self.f = open("歌曲详情.txt","a")
        #a表示追加写入，w表示覆盖写入
    def process_item(self, item, spider):
        num = len(item['title_list'])
        print(num)
        for i in range(num):
            play_count_str = item['play_count_list'][i].get()
            play_count_str2 = re.findall(r"\d+\.?\d*", play_count_str)[0]

            title_list_str = item['title_list'][i].get()
            artist_name_str = item['artist_name_list'][i].get()
            album_name_str = item['album_name_list'][i].get()
            song_str = title_list_str+"  "+artist_name_str+"  "+album_name_str+"  "+play_count_str2
            self.f.write(song_str+"\n")
            print(song_str+"正在保存...")
        self.f.write("----------------------------\n")
        return item
    #爬取结束的时候执行此方法，可以省去不写(固定方法)
    def close_spider(self,spider):
        self.f.close()
        spider.crawler.engine.close_spider(spider, '没有新数据关闭爬虫')
