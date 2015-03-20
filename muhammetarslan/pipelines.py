# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MuhammetarslanPipeline(object):

    def process_item(self, item, spider):

    	if item["title"]:

    		item["title"] = item["title"] + " - Pipeline Testi"

    		print item

    		return item

    	else:

    		raise DropItem("%s üründe title bilgisi yok" % item) 

class MySQLStorePipeline(object):

	def __init__(self):
		self.conn = MySQLdb.connect(user='root', passwd='muhammet123aa', db='test', host='localhost', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):    
	    try:
	        self.cursor.execute("""INSERT INTO posts (title, description)  
	                        VALUES (%s, %s)""", 
	                       (item['title'].encode('utf-8'), 
	                        item['description'].encode('utf-8')))

	        self.conn.commit()


	    except MySQLdb.Error, e:
	        print "Hata %d: %s" % (e.args[0], e.args[1])


	    return item
   
