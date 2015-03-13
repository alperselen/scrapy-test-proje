import scrapy


class MuhammetarslanItem(scrapy.Item):
     
    post_id= scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
