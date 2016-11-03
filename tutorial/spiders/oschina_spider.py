# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import OschinaItem

class OschinaSpider(scrapy.Spider):
	name = "oscspider"
	allowed_domains = ["dmoz.org"];
	start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	];

	def parse(self, response):
		# filename = response.url.split("/")[-2];
		# with open(filename, 'wb') as f:
		# 	f.write(response.body)

		for sel in response.xpath('//ul/li'):
			# title = sel.xpath('a/text()').extract()
			# link = sel.xpath('a/@href').extract()
			# desc = sel.xpath('text()').extract
			# print "#out#####", title, link, desc

			item = OschinaItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			yield item
