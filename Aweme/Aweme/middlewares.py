# coding=utf-8
import random

"""
不加UA可以访问，但个别url没有数据；
代理使用芝麻代理，可以使用redis库进行存储；
访问开启重试，超时情况下更换代理重新访问
"""
proxy_list = [
    "http://49.87.119.6:4261",
    "http://171.125.14.161:6996",
    "http://117.90.84.81:4203",
    "http://119.85.3.225:4242",
    "http://175.165.211.91:4274",
    "http://220.178.146.185:4251",
    "http://117.94.70.43:5676",
    "http://58.22.204.22:4293",
    "http://171.125.14.48:4278",
    "http://60.219.217.165:1648",
    "http://171.122.196.140:4208",
    "http://118.120.218.44:4257",
    "http://119.114.239.254:1767",
    "http://144.255.15.152:3937",
    "http://175.4.112.172:7524",
    "http://123.12.233.29:2991",
    "http://58.243.15.106:4227",
    "http://122.242.63.96:4256",
    "http://115.210.24.174:4242",
    "http://60.184.112.133:4208",
    "http://114.103.169.186:4235",
    "http://125.121.131.49:4217",
    "http://106.111.209.134:5521",
    "http://182.244.169.30:4265",
    "http://175.44.108.202:4254",
    "http://49.88.249.95:2444",
    "http://112.83.91.1:2589",
    "http://114.103.115.63:4248",
    "http://106.56.245.37:4237",
    "http://117.84.63.224:4263",
    "http://117.94.64.203:5676",
    "http://121.231.155.69:4252",
    "http://122.242.41.74:4256",
    "http://112.84.52.10:4278",
    "http://106.226.237.161:5632",
    "http://112.113.161.160:4256",
    "http://114.219.131.68:2589",
    "http://144.0.99.103:4258",
    "http://175.42.158.213:4254",
    "http://115.221.12.234:2316",
]


# 随机UA
class AwemeUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = "Dalvik/2.1.0 (Linux; U; Android 8.1.0; EML-AL00 Build/HUAWEIEML-AL00)"
        request.headers['User-Agent'] = ua


# 代理中间件
class AwemeProxyMiddleware(object):
    def process_request(self, request, spider):
        ip = random.choice(proxy_list)
        request.meta['proxy'] = ip
        print(request.meta['proxy'])

    def process_response(self, request, response, spider):
        """对返回的response处理"""
        if response.status != 200:
            ip = random.choice(proxy_list)
            print("this is response ip:" + ip)
            request.meta['proxy'] = ip
            return request
        return response

    def process_exception(self, request, exception, spider):
        # 出现异常时（超时）使用代理
        print("\n出现异常，正在使用代理重试....\n")
        ip = random.choice(proxy_list)
        request.meta['proxy'] = ip
        return request


if __name__ == '__main__':
    a = AwemeProxyMiddleware()
