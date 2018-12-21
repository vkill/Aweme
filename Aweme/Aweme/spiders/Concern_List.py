# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Environment: Python3.6.1
import json
import logging
import math
import re
import time
import scrapy
from scrapy import log

from item.Likes_info_Item import ConcernInfoItem
from querydata import QueryUserId, QueryMaxTime
from tools import Encrypt

"""
需求：爬取KOL用户关注列表
方式：根据uid拼接抓取url，并用max_time进行翻页，url中的max_time是上一页返回数据中的min_time；
      并根据max_time来控制增量爬取，存入到MySQL中
数据库：userinfo_concern_id表
注：因数据限制，用户数据只能抓取到一部分
"""
class AwemeInfoSpider(scrapy.Spider):
    name = 'ConcernList'
    redis_key = 'likelist_url'
    def __init__(self, *args, **kwargs):
        super(AwemeInfoSpider, self).__init__(*args, **kwargs)
        self.User_ID_List = QueryUserId.QueryUserId().get_user_id()
        self.base_url = 'https://aweme.snssdk.com'
        self.api = '/aweme/v1/user/following/list/'
        self.params1 = "user_id={}"
        self.params2 = "&max_time={}"
        self.params3 = "&count=20&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=ALP-AL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=1024*576&dpi=192&update_version_code=1832&_rticket=1536744989405&ts=1536744990&as=a1a5dde97e81fbfea84355&cp=d31aba58ec819ee6e1McUg&mas=00a8422d39d7eb28de04f7adaffd1292f0acaccc2c1c86a6664666"
        self.current_time = math.floor(time.time())
        self.url = self.base_url + self.api + "?" + self.params1 + self.params2.format(
            self.current_time) + self.params3

        query = QueryMaxTime.QueryMaxTime()
        self.max_time = query.get_concern_max_time()

    # 遍历url并请求访问
    def start_requests(self):
        for user_id in self.User_ID_List:
            initial_url = self.url.format(user_id[0])
            start_url = Encrypt.get_aweme_token(initial_url)  # 获取加密参数cp as mas
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 meta={'url': start_url})

    # 解析响应json数据
    def parse(self, response):
        try:
            data = json.loads(response.body.decode())
            print('data:',data)
            concern_lists = data["followings"]
            # 判断是否有下一页的参数
            has_more = data["has_more"]
            maxtime = re.search("max_time=(\d+)",
                                response.url).group(1)
            if int(maxtime) > self.max_time:
                for concern_list in concern_lists:
                    item = ConcernInfoItem()
                    item["concern_id"] = concern_list["uid"]
                    item['uid'] = re.search('user_id=(\d+)',
                                            response.url).group(1)
                    item['max_time'] = maxtime
                    item['effective'] = 1
                    item["pytime"] = time.time()
                    # print(item)
                    yield item

                if has_more:
                    # 下一页url中的"max_time"为上一次json数据中的"min_time"
                    max_time = str(data["min_time"])
                    url = re.sub("max_time=(\d+)", "max_time=" + max_time,
                                 response.url)
                    print("response.meta['url']:", response.meta['url'])
                    # 重新获取mas和as加密参数，返回下一页url
                    next_start_url = Encrypt.get_aweme_token(url)

                    yield scrapy.Request(url=next_start_url,
                                         callback=self.parse,dont_filter=True,
                                         meta={'url': next_start_url})
        except Exception as error:
            log.error(error)
            print("max_time：" + str(re.search("max_time=(\d+)",
                                              response.url).group(1)))
            print("用户ID：" + str(re.search('user_id=(\d+)',
                                          response.url).group(1)))
