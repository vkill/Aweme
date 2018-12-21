# coding = utf-8
from tools import DBHelper


class QueryCreateTime(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_create_time(self, aweme_id):
        # 根据作品id查询对应create_time最大值
        self.db_helper.connect_database()
        query_sql = "SELECT MAX(create_time) FROM works_comment WHERE aweme_id = %s" % aweme_id
        result = self.db_helper.query_task(query_sql)[0][0]
        if result:
            return result
        else:
            return 0


if __name__ == '__main__':
    query = QueryCreateTime()
    a = query.get_create_time(aweme_id=6609101290280586509)
    print(a)
    print(type(a))
