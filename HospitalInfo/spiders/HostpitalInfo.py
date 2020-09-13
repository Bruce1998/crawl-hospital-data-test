# -*- coding: utf-8 -*-
import scrapy
import logging
from HospitalInfo.items import HospitalinfoItem

logger = logging.getLogger('SpiderLogger')
class HospitalinfoSpider(scrapy.Spider):
    name = 'HostpitalInfo'
    start_urls = ['http://www.pharmnet.com.cn/search/yljg/']

    #解析首页
    def parse(self, response):
        lis = response.css('div[class="state"]').css('ul li')
        for li in lis:
            href = li.css('::attr(href)').extract_first()
            yield scrapy.Request(url=href, callback=self.parse_province)
    
    #解析第二级
    def parse_province(self, response):
        div = response.css('div[class="city"]')
        link = div.css('li').css('::attr(href)').extract_first()
        if (link != None):
            logger.info(link)
            yield scrapy.Request(url=link, callback=self.parse_city)

    #解析第三级
    def parse_city(self,response):
        item = HospitalinfoItem()
        tables = response.css('td[valign="top"][align="center"]').css('table')[1:-3]
        for data in tables:
            item['name'] = data.css('td[class="txt"] font u::text').extract_first()
            tds = data.css('td[valign="top"]').css('td')
            try:
                item['address'] = tds[2].css('::text').extract_first()
                item['post_code'] = tds[4].css('::text').extract_first()
                item['phone'] = tds[6].css('::text').extract_first()
                item['bed_num'] = tds[8].css('::text').extract_first()
            except IndexError:
                item['address'] = ''
                item['post_code'] = ''
                item['phone'] = ''
                item['bed_num'] = ''
            yield item
