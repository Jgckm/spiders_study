# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from fake_useragent import UserAgent

class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.



    # 拦截请求
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        # UA伪装
        request.headers['User-Agent'] = UserAgent().random
        print(request.headers['User-Agent'])
        # request.meta['proxy'] = 'http://221.4.241.198:9091'

        return None

    # 拦截响应
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    # 拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain

        # 判断http进行代理
        # if request.url.split(':')[0] == 'http':
        #     request.meta['proxy'] = random.choice(self.proxy_http)
        # else:
        #     request.meta['proxy'] = random.choice(self.proxy_https)

        # 错误是尝试代理
        # request.meta['proxy'] = 'http://221.4.241.198:9091'
        # 将修正后的请求对象进行重新的请求发送
        return request


