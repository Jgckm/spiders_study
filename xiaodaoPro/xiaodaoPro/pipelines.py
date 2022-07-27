# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class XiaodaoproPipeline:
    fp = None

    # 重写父类方法的一个方法：发方法只在开始爬虫的时候被调用一次
    def open_spider(self, spider):
        print('开始爬虫.....')
        self.fp = open('./xiaodao.txt', 'w', encoding='utf-8')

    # 专门处理item类型对象
    # 该方法可以接收到爬虫文件提交过来的item对象
    def process_item(self, item, spider):
        title = item['title']

        self.fp.write(title + '\n')

        return item # 就会传递给下一个即将被执行的管道类

    def close_spider(self,spider):
        print('结束爬虫...')
        self.fp.close()


# 管道文件中个管道类对应将以一组数据存储到一个平台或者载体中
class MysqlPipeLine:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='admin123', db='data')

    def process_itme(self, item, spider):
        # 创建服务器游标
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into xiaodao values("%s")%(item["title"])')
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item # 就会传递给下一个即将被执行的管道类

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

# 爬虫文件提交的item类型的对象最终会提交给哪一个管道？
