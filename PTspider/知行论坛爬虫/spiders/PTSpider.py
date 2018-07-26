# -*- coding: utf-8 -*-
import scrapy
from properties.items import PTItem
import logging

class PTSpider(scrapy.Spider):

    name = 'PTSpider'
    allowed_domains= ['pt.zhixing.bjtu.edu.cn']
    start_urls = ['http://pt.zhixing.bjtu.edu.cn/search/movie/']
    def start_requests(self):
        start_url = 'http://pt.zhixing.bjtu.edu.cn/search/movie/'
        cookie = {'zhixing_9328_saltkey': 'B0VvBA6e', 'zhixing_9328_lastvisit': '1524486980', 'zhixing_9328_ulastactivity': 'c7e6nXNDbSCpzXLDrFQSYU3eWe%2FYBNwMrk35h%2Bka2KIHNFVntWP1', 'zhixing_9328_lastcheckfeed': '370574%7C1524490793', 'PHPSESSID': '7oqrotgdlg6p2en8q4548vegj2', 'zhixing_9328_lip': '2001%3Ada8%3A205%3A40b1%3A682f%3Ac449%3A526b%3A8225%2C1524537429', 'cgbt_uid': '27e988ddb020dd7d2a090393aae8aa5245933558rzpcJyjkOguyuSPWkbqtKKyah1q55a6j', 'cgbt_password': '3056e6b8fcefd69fb27ef5c0bf9c65595812d88cNLLD5ZyjqfzRF5dv%2FVnpRL7dKk5qFIHsQmOXe%2BqTJXQ79wm2eUTYFy45rCt1LHa63zmGLwMgIk0TfJ92', 'zhixing_9328_sid': 'Ro2M4f', 'zhixing_9328_lastact': '1524538073%09uc.php%09', 'zhixing_9328_auth': '0cbfC0lQ%2BVGkZA7LxRZz0ZR3pk2I3QOKzZ%2BpiagnYbQBL29IbJtnu%2Fox2h%2FMaDVAhpFhtu1GOSanGg3S5Y0%2BmIxJlRI'}

        headers = {
            'Connection' : 'keep - alive',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            ,'Host': 'pt.zhixing.bjtu.edu.cn',
            'Referer': 'http://pt.zhixing.bjtu.edu.cn/search/',
            'Upgrade-Insecure-Requests': '1'
        }
        yield scrapy.Request(url=start_url,headers=headers,cookies=cookie)
        #yield scrapy.Request(url=start_url, headers=headers)
    def parse(self, response):
        item=PTItem()
        #for box in response.xpath('//*[@class="l"]'):
            #item['movie']=box.xpath('.//*[@name="title"]/text()').extract()
            
            #item['url']=box.xpath('./a/@href').extract()
            #urls=''#'http://pt.zhixing.bjtu.edu.cn'+ 
            #x='http://pt.zhixing.bjtu.edu.cn'+item['url']
            
            #yield item
        for boxs in response.xpath('.//*[@class="torrenttable"]//tr'):
            item['downloadcount']=boxs.xpath('.//td[10]/text()').extract()
            item['movie']=boxs.xpath('.//*[@name="title"]/text()').extract()
            
            yield item
        url = response.xpath(".//*[@id='mainContent']/div[2]//*[@class='next']/@href").extract()
        if url :
            page = 'http://pt.zhixing.bjtu.edu.cn'+url[0] 
            #yield scrapy.Request(item['url'],meta={'item':item},callback=self.get_details,dont_filter=True)
            yield scrapy.Request(page, callback=self.parse)
    #def get_details(self,response):
        #for x in response.xpath("//*[@class='torrent-head-r']"):
            #item['downloadcount']=x.xpath('.//*[@type="torrent-detail-done"]/text()').extract()[2:end]
            #yield item
#//a[contains(text(),'next')]
