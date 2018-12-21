# Redis数据库地址
REDIS_HOST = '47.93.117.55'

# Redis端口
REDIS_PORT = 6379

# Redis库
REDIS_DB = 5

# Redis密码，如无填None
REDIS_PASSWORD = '1234qweR'

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50
# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 20

# 测试API，抓哪个网站测哪个
TEST_URL = 'https://www.baidu.com'

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10
