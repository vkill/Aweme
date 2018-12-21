# coding=utf-8
import scrapy


# 粉丝ID列表
class FansInfoItem(scrapy.Item):
    uid = scrapy.Field()  # 用户ID
    fans_id = scrapy.Field()  # 粉丝ID
    max_time = scrapy.Field()  # 本页爬虫最大创建时间
    effective = scrapy.Field()  # 粉丝是否有效，默认为1
    pytime = scrapy.Field()  # 爬虫开始时间

    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = """INSERT INTO userinfo_fans_id(uid , fans_id , max_time , effective) VALUES (%s, %s, %s, %s)"""
        params = (self['uid'], self['fans_id'], self['max_time'],
                  self['effective'])
        return insert_sql, params

    # 数据库去重
    def distinct_data(self):
        query = """select fans_id from userinfo_fans_id where fans_id =%s"""
        params = (self["fans_id"])
        return query, params
