import scrapy
from xiaodaoPro.items import XiaodaoproItem


class XiaodaoSpider(scrapy.Spider):
    name = 'xiaodao'
    # allowed_domains = ['www.xxxx.com']
    start_urls = ['https://xd.x6d.com/']

    # def parse(self, response):
    #     # xpath 返回的是列表 ，但是列表元素一定是Selector类型的对象
    #     # get 可以 Selector对象中data参数存储的字符串提取出来
    #     li_list = response.xpath('//div[@id="newslist"]/ul/li')
    #     # 列表调用了get之后 ，则表示列表中每一个Selector对象中的data的对应的字符串提取出来
    #     all_data = []  # 存储所有解析到的数据
    #     for li in li_list:
    #         title = li.xpath('./a/text()').get()
    #         print(title)
    #         data = {
    #             'title': title
    #         }
    #         all_data.append(data)
    #     return all_data

    def parse(self, response):
        # xpath 返回的是列表 ，但是列表元素一定是Selector类型的对象
        # get 可以 Selector对象中data参数存储的字符串提取出来
        li_list = response.xpath('//div[@id="newslist"]/ul/li')
        # 列表调用了get之后 ，则表示列表中每一个Selector对象中的data的对应的字符串提取出来
        item = XiaodaoproItem()
        for li in li_list:
            title = li.xpath('./a/text()').get()
            print(title)
            item['title'] = title.strip()

            yield item  # 将item提交给了管道