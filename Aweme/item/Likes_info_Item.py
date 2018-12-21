# coding=utf-8
import scrapy


# 关注ID列表
class ConcernInfoItem(scrapy.Item):
    uid = scrapy.Field()  # 用户ID
    concern_id = scrapy.Field()  # 关注用户ID
    max_time = scrapy.Field()  # 本页项目最大创建时间
    begin_time = scrapy.Field()  # 爬虫开始时间
    effective = scrapy.Field()  # 是否有效，默认为1
    pytime = scrapy.Field()

    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = """INSERT INTO userinfo_concern_id(uid , concern_id , max_time , effective) VALUES (%s, %s, %s, %s)"""
        params = (self['uid'], self['concern_id'], self['max_time'],
                  self['effective'])
        return insert_sql, params

    # 数据库去重
    def distinct_data(self):
        query = """select concern_id from userinfo_concern_id where concern_id =%s"""
        params = (self["concern_id"])
        return query, params
