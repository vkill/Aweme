# coding = utf-8


# 作品列表信息
import scrapy


class AwemeInfoItem(scrapy.Item):
    author_user_id = scrapy.Field()  # 作者ID
    aweme_id = scrapy.Field()  # 作品ID
    aweme_type = scrapy.Field()  # 作品类型
    create_time = scrapy.Field()  # 创建时间
    duration = scrapy.Field()  # 持续时间
    des = scrapy.Field()  # 作品描述
    digg_count = scrapy.Field()  # 点赞数
    comment_count = scrapy.Field()  # 评论数
    share_count = scrapy.Field()  # 转发数

    is_ads = scrapy.Field()  # 是否是广告
    is_fantasy = scrapy.Field()
    is_hash_tag = scrapy.Field()
    is_pgcshow = scrapy.Field()  # 是否为pgc显示
    is_relieve = scrapy.Field()
    is_top = scrapy.Field()  # 是否置顶
    is_vr = scrapy.Field()  # 是否是VR视频
    item_comment_settings = scrapy.Field()  # 评论设置
    prevent_download = scrapy.Field()  # 是否禁止下载
    rate = scrapy.Field()  # 比率
    region = scrapy.Field()  # 区域
    share_url = scrapy.Field()  # 分享链接
    sort_label = scrapy.Field()  # 分类标签

    # 背景音乐信息
    # album = scrapy.Field()  # 音乐专辑
    owner_nickname = scrapy.Field()  # 音乐作者
    title = scrapy.Field()  # 背景音乐名称
    author = scrapy.Field()  # 背景音乐作者
    is_del_video = scrapy.Field()  # 作者是否删除
    collect_stat = scrapy.Field()  # 值为0
    cover_hd = scrapy.Field()  # 封面高清图片地址
    cover_large = scrapy.Field()  # 封面大图地址
    cover_medium = scrapy.Field()  # 封面中图地址
    cover_thumb = scrapy.Field()  # 封面小图地址
    is_original = scrapy.Field()  # 是否为原创
    music_id = scrapy.Field()  # 音乐ID
    is_restricted = scrapy.Field()  # 是否保密
    is_video_self_see = scrapy.Field()  # 是否只有自己可看
    mid = scrapy.Field()  # mid
    owner_handle = scrapy.Field()  # 作者自定义ID
    owner_id = scrapy.Field()  # 作者ID
    offline_desc = scrapy.Field()  # 线下描述
    play_url = scrapy.Field()  # 音乐播放地址
    source_platform = scrapy.Field()  # 来源平台？
    status = scrapy.Field()  # 状态
    user_count = scrapy.Field()  # 使用数量
    redirect = scrapy.Field()  # 是否重定向
    video_labels = scrapy.Field()  # 视频标签
    audio_track = scrapy.Field()  # 音轨地址

    # 视频信息
    bit_rate = scrapy.Field()  # 比特率
    height = scrapy.Field()  # 视频高度
    width = scrapy.Field()  # 视频宽度
    origin_cover = scrapy.Field()  # 原始封面
    has_watermark = scrapy.Field()  # 有无水印
    ratio = scrapy.Field()  # 清晰度
    play_addr_url = scrapy.Field()  # 视频播放url
    play_addr_uri = scrapy.Field()  # 视频播放uri
    url_key = scrapy.Field()  # 视频key
    download_addr = scrapy.Field()  # 视频下载地址
    dynamic_cover = scrapy.Field()  # 动态封面

    # 风险信息
    content = scrapy.Field()
    risk_sink = scrapy.Field()
    type = scrapy.Field()
    warn = scrapy.Field()
    vote = scrapy.Field()

    # 增量爬取字段
    max_cursor = scrapy.Field()

    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = "INSERT INTO works(aweme_id , author_user_id , aweme_type , create_time , duration , des , digg_count , comment_count , share_count , is_ads , " \
              "is_hash_tag , is_pgcshow ,is_relieve ,is_top ,is_vr , item_comment_settings , prevent_download ,rate , region , share_url ," \
              "sort_label , music_owner_nickname , music_author , music_is_del_video ,music_cover_thumb ,music_is_original ,music_id, music_is_restricted ,music_is_video_self_see, music_mid ," \
              "music_owner_handle , music_owner_id , music_offline_desc , music_play_url , music_source_platform , music_title , music_user_count , music_redirect , music_audio_track ,video_origin_cover ," \
              "video_height ,video_width ,video_has_watermark ,video_ratio ,video_play_addr_uri ,video_play_addr_url ,video_url_key ,video_download_addr ,video_dynamic_cover ,risk_content ," \
              "risk_sink ,risk_type ,risk_warn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (
            self['aweme_id'], self['author_user_id'],
            self['aweme_type'],
            self['create_time'], self['duration'], self['des'],
            self['digg_count'], self['comment_count'],
            self['share_count'],
            self['is_ads'],
            self['is_hash_tag'], self['is_pgcshow'], self['is_relieve'],
            self['is_top'], self['is_vr'],
            self['item_comment_settings'],
            self['prevent_download'], self['rate'], self['region'],
            self['share_url'],
            self['sort_label'], self['owner_nickname'],
            self['author'], self['is_del_video'],
            self['cover_thumb'], self['is_original'],
            self['music_id'], self['is_restricted'],
            self['is_video_self_see'], self['mid'],
            self['owner_handle'], self['owner_id'],
            self['offline_desc'], self['play_url'],
            self['source_platform'], self['title'],
            self['user_count'], self['redirect'],
            self['audio_track'], self['origin_cover'],
            self['height'], self['width'],
            self['has_watermark'], self['ratio'],
            self['play_addr_uri'], self['play_addr_url'],
            self['url_key'], self['download_addr'],
            self['dynamic_cover'], self['content'],
            self['risk_sink'], self['type'], self['warn'])
        return insert_sql, params

    # 数据库去重
    def distinct_data(self):
        query = """select id from works where id =%s"""
        params = (0,)
        return query, params
