# coding=utf-8
import scrapy


# 用户粉丝总数与关注总数
class FansConcernItem(scrapy.Item):
    uid = scrapy.Field()
    aweme_fans_count = scrapy.Field()  # 发布作品总数
    following_count = scrapy.Field()  # 收藏作品总数
    aweme_count = scrapy.Field()  # 粉丝用户总数
    favoriting_count = scrapy.Field()  # 收藏用户总数

    def get_insert_sql(self):
        insert_sql = """INSERT INTO userinfo_concern(uid ,aweme_fans_count,following_count,aweme_count, favoriting_count) VALUES (%s, %s, %s, %s, %s)"""
        params = (self['uid'], self['aweme_fans_count'], self['following_count'], self['aweme_count'], self['favoriting_count'])
        return insert_sql, params
    def distinct_data(self):
        query = """select uid from userinfo_concern where uid =%s"""
        params = (0,)
        return query, params
