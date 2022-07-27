import scrapy


class BiantuSpider(scrapy.Spider):
    name = 'biantu'
    # allowed_domains = ['www.bian']
    start_urls = ['https://pic.netbian.com/e/search/result/?searchid=2543']

    # 生成一个 url 模板 https://pic.netbian.com/e/search/result/index.php?page=0&searchid=2543
    url = 'https://pic.netbian.com/e/search/result/index.php?page=%d&searchid=2543'
    page_num = 1

    def parse(self, response):
        li_lsit = response.xpath('//*[@id="main"]/div[2]/ul/li')
        for li in li_lsit:
            img_name = li.xpath('./a/b/text()').get()
            print(img_name)

        if self.page_num <= 10:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            print(new_url)
            # 手动发送请求
            yield scrapy.Request(url=new_url, callback=self.parse)
