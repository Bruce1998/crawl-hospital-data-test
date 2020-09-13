# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HospitalinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    
    address = scrapy.Field()
    post_code = scrapy.Field()
    phone = scrapy.Field()
    bed_num = scrapy.Field()
