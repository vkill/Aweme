# coding = utf-8

# coding=utf-8
from tools import DBHelper


class QueryMaxTime(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_fans_max_time(self):
        # 查询粉丝列表max_time最大值
        self.db_helper.connect_database()
        query_sql = "SELECT MAX(max_time) FROM userinfo_fans_id"
        result = self.db_helper.query_task(query_sql)[0][0]
        if result:
            max_time = int(result)
        else:
            max_time = 0
        return max_time

    def get_concern_max_time(self):
        # 查询关注列表max_time最大值
        self.db_helper.connect_database()
        query_sql = "SELECT MAX(max_time) FROM userinfo_concern_id"
        result = self.db_helper.query_task(query_sql)[0][0]
        if result:
            max_time = int(result)
        else:
            max_time = 0
        return max_time


if __name__ == '__main__':
    query = QueryMaxTime()
    a = query.get_fans_max_time()
    b = query.get_concern_max_time()
    print(a)
    print(b)
