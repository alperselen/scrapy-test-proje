#!/usr/bin/python
#-*-coding:utf-8-*-

import scrapy

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from muhammetarslan.items import MuhammetarslanItem


from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import re
import urlparse

class Muhammetarslanspider(CrawlSpider):
    name = "muhammetarslanspider"

    def __init__(self):
        
        
        self.allowed_domains = ["muhammetarslan.com","www.muhammetarslan.com"]
        self.start_urls = [
        "http://www.muhammetarslan.com",
        ]

        self.rules = [
            Rule(SgmlLinkExtractor(allow='(.*)\muhammetarslan\.com\/(.*)$'), callback='parse_items',follow = True),
            Rule(SgmlLinkExtractor(allow=()),follow=True),
            ]


           
  

        super(Muhammetarslanspider, self).__init__()

    def parse_items(self, response):
        
       
        item = MuhammetarslanItem()
        sel = Selector(response)


        id = sel.xpath('//input[@id="comment_post_ID"]/@value').extract()
        if id:

        	id = id.pop().strip()
        	title = sel.xpath('//h1[@class="heading"]//a/text()').extract().pop().strip()
        	description = sel.xpath('//div[@class="entry"]').extract().pop().strip()

        	item["post_id"] = id
        	item['title'] = title
        	item['description'] = description

        	yield item
