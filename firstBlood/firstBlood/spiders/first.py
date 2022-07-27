import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件名称 爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名：用来限制 start_urls列表中哪些请求可以进行发送
    # allowed_domains = ['www.xxx.com']

    # 起始地url 列表:该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://www.baidu.com/','https://www.sogou.com/']

    # 用作于数据解析：response表示的就是请求后对应的响应数据
    def parse(self, response):
        print(response)
