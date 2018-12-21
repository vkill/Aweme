# coding=utf-8
import scrapy
from scrapy import Item


class UserLikeAwemeItem(Item):
    uid = scrapy.Field()  # 用户ID
    like_aweme_id = scrapy.Field()  # 用户喜欢作品ID

    def get_insert_sql(self):
        insert_sql = """INSERT INTO user_like_aweme_id(uid,like_aweme_id) VALUES (%s, %s)"""
        params = (self['uid'], self['like_aweme_id'])
        return insert_sql, params

    # 数据库去重
    def distinct_data(self):
        query = """select like_aweme_id from user_like_aweme_id where uid =%s and like_aweme_id=%s"""
        params = (self['uid'], self['like_aweme_id'])
        return query, params
