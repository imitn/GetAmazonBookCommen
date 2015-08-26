# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class GetamazonbookcommenItem(Item):
    common = Field() #评论内容
