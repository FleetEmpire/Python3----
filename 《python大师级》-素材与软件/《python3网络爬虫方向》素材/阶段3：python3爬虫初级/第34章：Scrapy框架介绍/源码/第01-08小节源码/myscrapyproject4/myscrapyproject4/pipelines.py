# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#管道文件，进行数据的处理和保存
class Myscrapyproject4Pipeline:
    def process_item(self, item, spider):
        #item:从爬虫中传递的item
        #对数据进行操作
        print(item)
        return item
