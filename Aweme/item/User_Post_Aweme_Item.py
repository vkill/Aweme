# coding=utf-8
import scrapy
from scrapy import Item


class UserPostAwemeItem(Item):
    uid = scrapy.Field()  # 用户ID
    post_aweme_id = scrapy.Field()  # 用户发表作品ID

    def get_insert_sql(self):
        insert_sql = """INSERT INTO user_post_aweme_id(uid,post_aweme_id) VALUES (%s, %s)"""
        params = (self['uid'], self['post_aweme_id'])
        return insert_sql, params

    # 数据库去重
    def distinct_data(self):
        query = """select post_aweme_id from user_post_aweme_id where uid =%s and post_aweme_id=%s"""
        params = (self['uid'], self['post_aweme_id'])
        return query, params
