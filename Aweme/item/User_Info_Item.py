# coding = utf-8

# 用户个人信息
import scrapy


class UserInfoItem(scrapy.Item):
    nickname = scrapy.Field()  # 用户名
    uid = scrapy.Field()  # 用户ID
    short_id = scrapy.Field()  # 用户短ID
    unique_id = scrapy.Field()  # 自定义ID
    unique_id_modify_time = scrapy.Field()  # 自定义ID修改时间
    total_favorited = scrapy.Field()  # 抖音总获赞数
    aweme_fans_count = scrapy.Field()  # 抖音粉丝数
    aweme_apple_id = scrapy.Field()  # 抖音apple_id
    toutiao_fans_count = scrapy.Field()  # 头条粉丝数
    toutiao_apple_id = scrapy.Field()  # 头条apple_id
    live_stream_aweme_fans_count = scrapy.Field()  # 火山小视频粉丝数
    live_stream_apple_id = scrapy.Field()  # 火山apple_id
    aweme_count = scrapy.Field()  # 抖音作品数量
    favoriting_count = scrapy.Field()  # 抖音喜欢作品数
    following_count = scrapy.Field()  # 抖音关注总数

    gender = scrapy.Field()  # 性别
    avatar_larger_url = scrapy.Field()  # 头像url
    avatar_larger_uri = scrapy.Field()  # 头像uri
    weibo_name = scrapy.Field()  # 绑定微博
    school_name = scrapy.Field()  # 学校名称
    school_poi_id = scrapy.Field()  # 学校POI ID
    school_type = scrapy.Field()  # 学校类型
    location = scrapy.Field()  # 位置
    birthday = scrapy.Field()  # 出生日期
    constellation = scrapy.Field()  # 星座
    city = scrapy.Field()  # 城市
    signature = scrapy.Field()  # 个性签名
    login_platform = scrapy.Field()  # 登录方式

    realname_verify_status = scrapy.Field()  # 实名验证状态
    is_block = scrapy.Field()  # 是否被锁
    custom_verify = scrapy.Field()  # 个人认证
    verify_info = scrapy.Field()  # 认证信息
    is_ad_fake = scrapy.Field()  # 是否是假广告？
    is_gov_media_vip = scrapy.Field()  # 是否是政府单位媒体
    is_verified = scrapy.Field()  # 是否验证过
    live_agreement = scrapy.Field()  # 合同？
    live_verify = scrapy.Field()  # 线下认证？
    enterprise_verify_reason = scrapy.Field()  # 企业认证原因
    commerce_user_level = scrapy.Field()  # 商务等级

    user_canceled = scrapy.Field()  #
    with_commerce_entry = scrapy.Field()  #
    with_dou_entry = scrapy.Field()  #
    with_douplus_entry = scrapy.Field()  #
    with_fusion_shop_entry = scrapy.Field()  #
    with_new_goods = scrapy.Field()  #
    with_shop_entry = scrapy.Field()  #
    need_recommend = scrapy.Field()  #
    room_id = scrapy.Field()  #
    special_lock = scrapy.Field()  #
    pytime = scrapy.Field()

    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = (
            "INSERT INTO userinfo(nickname,uid,short_id,unique_id,unique_id_modify_time,total_favorited,aweme_fans_count,aweme_apple_id,toutiao_fans_count,toutiao_apple_id,live_stream_aweme_fans_count,live_stream_apple_id,aweme_count,favoriting_count,gender,avatar_larger_uri, avatar_larger_url, weibo_name,school_name,school_poi_id,school_type,location,birthday,constellation ,city , signature , login_platform ,realname_verify_status , is_block , custom_verify , is_ad_fake , is_gov_media_vip , live_agreement,live_verify,enterprise_verify_reason,commerce_user_level,user_canceled,with_commerce_entry,with_dou_entry,with_douplus_entry,with_shop_entry,with_new_goods,with_fusion_shop_entry,need_recommend,room_id,special_lock) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        params = (self['nickname'], self['uid'], self['short_id'],
                  self['unique_id'], self['unique_id_modify_time'],
                  self['total_favorited'], self['aweme_fans_count'],
                  self['aweme_apple_id'], self['toutiao_fans_count'],
                  self['toutiao_apple_id'],
                  self['live_stream_aweme_fans_count'],
                  self['live_stream_apple_id'], self['aweme_count'],
                  self['favoriting_count'], self['gender'],
                  self['avatar_larger_uri'], self['avatar_larger_url'],
                  self['weibo_name'], self['school_name'],
                  self['school_poi_id'],
                  self['school_type'], self['location'],
                  self['birthday'], self['constellation'],
                  self['city'],
                  self['signature'], self['login_platform'],
                  self['realname_verify_status'], self['is_block'],
                  self['custom_verify'],
                  self['is_ad_fake'], self['is_gov_media_vip'],
                  self['live_agreement'], self['live_verify'],
                  self['enterprise_verify_reason'],
                  self['commerce_user_level'], self['user_canceled'],
                  self['with_commerce_entry'], self['with_dou_entry'],
                  self['with_douplus_entry'],
                  self['with_shop_entry'], self['with_new_goods'],
                  self['with_fusion_shop_entry'],
                  self['need_recommend'],
                  self['room_id'], self['special_lock'])
        return insert_sql, params

    def distinct_data(self):
        query = """select uid from userinfo where uid =%s"""
        params = (0,)
        return query, params
