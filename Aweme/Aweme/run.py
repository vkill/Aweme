# coding=utf-8
from scrapy import cmdline
cmdline.execute('scrapy crawl UserInfo'.split()) # 抓取KOL用户信息
# cmdline.execute('scrapy crawl FansList'.split()) # 抓取KOL粉丝列表
# cmdline.execute('scrapy crawl ConcernList'.split()) # 抓取KOL关注列表
# cmdline.execute('scrapy crawl Post_Aweme_Info'.split())  #抓取KOL发布作品列表
# cmdline.execute('scrapy crawl Like_Aweme_Info'.split()) #抓取KOL喜欢作品列表
# cmdline.execute('scrapy crawl CommentInfo'.split()) #抓取KOL作品评论信息
