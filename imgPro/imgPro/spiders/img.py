import scrapy
from scrapy.http import HtmlResponse
from urllib.parse import urljoin
from imgPro.items import ImgproItem

class ImgSpider(scrapy.Spider):

    name = 'img'
    # allowed_domains = ['img.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response: HtmlResponse, **kwargs):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            item = ImgproItem()
            src = div.xpath('./div/a/img/@src').get()
            item['src'] = urljoin(self.start_urls[0], src)
            yield item

