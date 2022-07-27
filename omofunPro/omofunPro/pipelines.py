# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib.parse import urljoin
from scrapy.http import Request
from scrapy import Selector
from json import loads


class OmofunproPipeline:
    def process_item(self, item, spider):

        return item

    # # 解析播放链接
    # def parse_player(self, response, **kwargs):
    #     item = response.meta['item']
    #     sel = Selector(response)
    #     player = sel.xpath('//div[@class="player-box-main"]/script[1]/text()').get()
    #     player_name = sel.xpath('//a[@class="module-play-list-link active"]/span/text()').get()
    #     try:
    #         player_str = loads(str(player).split('=')[1])['url']
    #     except:
    #         player_str = sel.xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div[2]/text()').get()
    #
    #     player_url = {
    #         "play_name": player_name,
    #         "play_url": player_str
    #     }
    #     item['player'] = player_url
    #     print(item)
    #     return item
