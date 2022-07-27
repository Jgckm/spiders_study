# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


# class ImgproPipeline:
#     def process_item(self, item, spider):
#         return item


class imgsPileLine(ImagesPipeline):

   #  就是可以根据图片地址进行数据请求的
   def get_media_requests(self, item, info):

       yield Request(item['src'])

   # 指定图片存储路径
   def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-1] # 定制图片名称
        return imgName

   def item_completed(self, results, item, info):
       return item # 返回给下一个要执行的管道
