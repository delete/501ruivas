# -*- coding: utf-8 -*-

# Scrapy settings for ruivas project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ruivas'

SPIDER_MODULES = ['ruivas.spiders']
NEWSPIDER_MODULE = 'ruivas.spiders'

ITEM_PIPELINES = ['ruivas.pipelines.RuivasPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ruivas (+http://www.yourdomain.com)'
