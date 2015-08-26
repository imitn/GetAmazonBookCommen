# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from GetAmazonBookCommen.items import GetamazonbookcommenItem
import math,time

class DmozSpider(Spider):
    name = "getcommons"
    allowed_domains = ["amazon.cn"]
    #添加要爬取的书籍的url，此处只爬取亚马逊《深入理解scala》的评论
    start_urls = [
        "http://www.amazon.cn/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3Scala-%E8%8B%8F%E7%91%9E%E8%8C%A8/dp/B00RS6C9F8/ref=sr_1_1?s=books&ie=UTF8&qid=1440579977&sr=1-1&keywords=scala",
    ]

    def parse(self, response):
   
        sel = Selector(response)
        commons = sel.xpath("//div[@class='a-section']")#分析页面，获取评论内容路径
        items = []

        filename=str(int(math.ceil(time.time())))+'.txt'#获取系统当前时间作为文件名
        with open(filename,'w+') as f:
            for c in commons:           
                item = GetamazonbookcommenItem()
                wordlist=c.xpath("text()").extract()#获取评论内容，一个列表保存一条评论

                line="".join(wordlist)#列表转换成字符串
                line="".join(line.split())#去掉字符串的回车换行空格等字符
                if line:#字符串不为空，则保存评论内容           
                    item['common']=line
                    items.append(item)  
                    f.write(line.encode('utf-8')+'\n')#保存一条评论并换行

        print items
