# -*- coding: utf-8 -*-
import scrapy


class ENorSpider(scrapy.Spider):
    name = 'e-nor'
    allowed_domains = ['e-nor.com']
    start_urls = ['http://e-nor.com/']

    def parse(self, response):
        pass
