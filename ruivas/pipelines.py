# -*- coding: utf-8 -*-
from urllib import urlopen
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

PATH = 'images/'

class RuivasPipeline(object):

    def __init__(self):
        if not os.path.isdir('images/'):
            os.mkdir('images')

    def process_item(self, item, spider):
        # Get the file name eg.  blablabla.jpg
        name = item['link'].split('/')[-1]
        
        if not os.path.isfile(PATH + name):
            with open(PATH + name, 'w') as file:
                file.write(urlopen(item['link']).read())            

        return item
