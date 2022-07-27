import scrapy
from scrapy.http import HtmlResponse


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['xxxxxxxx']
    start_urls = ['https://www.baidu.com/s?&wd=ip']

    def parse(self, response: HtmlResponse, **kwargs):
        page_text = response.text

        with open('ip.html', 'w', encoding='utf-8')as fp:
            fp.write(page_text)