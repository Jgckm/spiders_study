import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse, Request
from urllib.parse import urljoin
from omofunPro.items import OmofunproItem


class OmofunSpider(scrapy.Spider):
    name = 'omofun'
    # allowed_domains = ['wwwwww']
    start_urls = ['https://www.omofun.tv/vod/show/id/20/page/1.html']

    def parse(self, response: HtmlResponse, *kwargs):
        sel = Selector(response)
        a_list = sel.xpath('/html/body/div/div[3]/div/div/div[3]/div[1]/a')
        for a in a_list:
            item = OmofunproItem()
            detail_url = urljoin(self.start_urls[0], a.xpath('./@href').get())
            item['name'] = a.xpath('./@title').get()
            item['image_url'] = a.xpath('./div[1]/div[2]/img/@data-original').get()
            item['status'] = a.xpath('./div[1]/div[1]/text()').get()
            yield Request(url=detail_url, callback=self.parse_detail, meta={'item': item})


    # 解析详情页
    def parse_detail(self, response: HtmlResponse, **kwargs):
            item = response.meta['item']
            sel = Selector(response)
            item['id'] = response.url.replace('https://www.omofun.tv/vod/detail/id/','').replace('.html','')
            item['year'] = response.xpath('/html/body/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a/text()').get()
            item['detail'] = sel.xpath('/html/body/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div/p/text()').get()
            item['country'] = sel.xpath('/html/body/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/a/text()').get()
            item['type'] = sel.xpath('/html/body/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/a/text()').get()
            item['director'] = sel.xpath('/html/body/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/a/text()').get()
            item['actor'] = sel.xpath('/html/body/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div/a/text()').get()
            item['update'] = sel.xpath('/html/body/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div/text()').get()
            item['player'] = sel.xpath('//*[@id="panel1"]/div/div/a/@href').getall()
            yield item

