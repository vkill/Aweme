# coding = utf-8
import scrapy


# 评论信息
class CommentInfoItem(scrapy.Item):
    aweme_id = scrapy.Field()  # 作品ID
    create_time = scrapy.Field()  # 评论时间
    text = scrapy.Field()  # 评论内容
    user_id = scrapy.Field()  # 用户ID
    total = scrapy.Field()  # 评论总数
    digg_count = scrapy.Field()  # 评论点赞数
    cid = scrapy.Field()  # 评论ID
    status = scrapy.Field()  # 状态
    reply_id = scrapy.Field()  # 回复ID

    def get_insert_sql(self):
        insert_sql = """INSERT INTO works_comment(aweme_id ,create_time ,digg_count ,user_id ,cid ,text ,status ,reply_id ,total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        params = (self['aweme_id'], self['create_time'], self['digg_count'],
                  self['user_id'], self['cid'], self['text'], self['status'],
                  self['reply_id'], self['total'])
        return insert_sql, params

    def distinct_data(self):
        query = """select cid from works_comment where cid =%s"""
        params = (self["cid"])
        return query, params
