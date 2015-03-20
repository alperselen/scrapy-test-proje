# -*- coding: utf-8 -*-

# Scrapy settings for muhammetarslan project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'muhammetarslan'

SPIDER_MODULES = ['muhammetarslan.spiders']
NEWSPIDER_MODULE = 'muhammetarslan.spiders'

ITEM_PIPELINES = {

    'muhammetarslan.pipelines.MuhammetarslanPipeline': 800,
    'muhammetarslan.pipelines.MySQLStorePipeline':600,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'muhammetarslan (+http://www.yourdomain.com)'
