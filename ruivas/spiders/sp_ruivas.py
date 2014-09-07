# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ruivas.items import RuivasItem


class SpRuivasSpider(CrawlSpider):
    name = "sp_ruivas"
    allowed_domains = ["501ruivas.tumblr.com"]
    start_urls = (
        'http://501ruivas.tumblr.com/',
    )
    rules = (
        Rule(LinkExtractor(allow=("page/",), ), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        links_posts = response.xpath('//div[@class="post photo"]')
        items = []

        for l in links_posts:
            item = RuivasItem()
            try:
                item['link'] = l.xpath('div/a/img/@src').extract()[0]
            except IndexError:
                item['link'] = l.xpath('div/img/@src').extract()[0]
            items.append(item)
        
        return items
