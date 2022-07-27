import scrapy
from scrapy.http import HtmlResponse, Request
from jsonpath import jsonpath
from ..items import OmofunappItem



class OmofunappSpider(scrapy.Spider):
    name = 'omofunapp'
    # allowed_domains = ['api']
    start_urls = ['https://app.omofun.net/xgapp.php/v2/video?pg=1&tid=1&class=&area=&lang=&year=&rrrr=']

    def parse(self, response: HtmlResponse, **kwargs):
        data_josn = response.json()
        page = data_josn['pagecount']
        frommat_url = 'https://app.omofun.net/xgapp.php/v2/video?pg=%d&tid=1&class=&area=&lang=&year='
        for i in range(1, page + 1):
            url = format(frommat_url % i)
            yield Request(url=url, callback=self.parse_info)

    def parse_info(self, response: HtmlResponse):
        data = response.json()
        info = jsonpath(data, '$.data[0:]')
        for i in info:
            item = OmofunappItem()
            item['id'] = i['vod_id']
            item['name'] = i['vod_name']
            item['images'] = i['vod_pic']
            item['update'] = i['vod_time_add']
            item['remarks'] = i['vod_remarks']
            item['score'] = i['vod_score']
            url = f"https://app.omofun.net/xgapp.php/v2/video_detail?id={i['vod_id']}"
            print(item['name'])
            yield Request(url=url, callback=self.parse_player, meta={'item': item})

    def parse_player(self, response: HtmlResponse):
        item = response.meta['item']
        data = response.json()
        item['actor'] = jsonpath(data, '$.data..vod_actor')[0]
        item['blurb'] = jsonpath(data, '$.data..vod_blurb')[0].strip().replace('\t',  '').replace('\n', '').replace('\r', '')
        item['type'] = jsonpath(data, '$.data..vod_class')[0]
        item['country'] = jsonpath(data, '$.data..vod_area')[0]
        item['director'] = jsonpath(data, '$.data..vod_director')[0]
        item['year'] = jsonpath(data, '$.data..vod_year')[0]
        item['lang'] = jsonpath(data, '$.data..vod_lang')[0]
        player_list = jsonpath(data, '$.data..vod_url_with_player')[0]
        player_new_list = []
        for player in player_list:
            player.pop('code')
            player.pop('parse_api')
            player.pop('subtitle_field')
            player.pop('user_agent')
            player.pop('headers')
            player.pop('extra_parse_api')
            player.pop('un_link_features')
            player.pop('parse_after_config_enable')
            player.pop('parse_after_config_features')
            player.pop('link_features')
            player.pop('parse_after_config_user_agent')
            player.pop('parse_after_config_headers')
            player_new_list.append(player)
        item['player_list'] = player_new_list
        yield item
