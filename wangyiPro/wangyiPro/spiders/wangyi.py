import scrapy
from scrapy.http import HtmlResponse, Request
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']
    model_urls = []

    # 实例化一个浏览器对象
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "E:\Program Files (x86)\RunningCheeseChrome\App\chrome.exe"
        self.bro = webdriver.Chrome(executable_path='C:\\Users\Administrator\Desktop\scrapy\wangyiPro\chromedriver.exe', chrome_options=options)

    # 解析五大板块的详情url
    def parse(self, response: HtmlResponse, **kwargs):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [1, 2, 3, 4, 5]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').get()
            self.model_urls.append(model_url)

        for url in self.model_urls:
            yield Request(url, callback=self.model_parse)

    def model_parse(self, response: HtmlResponse):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/h3/a/@text').get()
            new_detail_url = div.xpath('./div/h3/a/@href').get()

            item = WangyiproItem()
            item['title'] = item
            # 对新闻详情页发起请求
            yield Request(url=new_detail_url, callback=self.detail_parse, meta={'item': item})

    def detail_parse(self, response:HtmlResponse): # 解析新闻内容
        item = response.meta['item']
        content = response.xpath('//*[@id="content"]/div[2]//text()').getall()
        content = ''.join(content)
        item['content'] = content

        yield item



