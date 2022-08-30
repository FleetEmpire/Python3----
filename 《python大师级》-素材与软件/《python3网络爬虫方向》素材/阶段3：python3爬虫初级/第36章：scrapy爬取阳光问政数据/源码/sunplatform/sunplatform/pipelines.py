# -*- coding: utf-8 -*-
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SunplatformPipeline:
    def __init__(self): #定义一些需要初始化的方法
        self.f = open("阳光问政条目.txt","a")
        #a表示追加写入，w表示覆盖写入
    def process_item(self, item, spider):
        title_str = item['title'].get()
        content_ask_str = item["content_ask"].get()
        content_answer_str = item["content_answer"].get()

        title_str = re.sub(r'<p class="focus-details">|</p>',"",title_str)
        content_ask_str = re.sub(r'<pre>|</pre>','',content_ask_str)
        content_answer_str = re.sub(r'<pre style="margin: 0;">|</pre>','',content_answer_str)

        sun_str = title_str + "\n" + content_ask_str + "\n" + content_answer_str+'\n'
        self.f.write(sun_str)
        print("正在保存...")
        self.f.write("----------------------------\n")
        return item
        # 爬取结束的时候执行此方法，可以省去不写(固定方法)

    def close_spider(self, spider):
        self.f.close()
        print("爬取完毕！")
        spider.crawler.engine.close_spider(spider, '没有新数据关闭爬虫')

