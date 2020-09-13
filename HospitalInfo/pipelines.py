# -*- coding: utf-8 -*-
import scrapy
from HospitalInfo.items import HospitalinfoItem
from scrapy.exporters import CsvItemExporter
import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

logger = logging.getLogger('PipelineLogger')
class HospitalinfoPipeline(object):

    def open_spider(self, spider):
        self.file = open('output.csv', 'wb+')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item