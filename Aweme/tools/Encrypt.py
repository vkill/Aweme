# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 11:52
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : Encrypt.py
# @Software: PyCharm
import time
import json
import requests
import hashlib
from urllib.parse import urlparse, parse_qs, urlencode


def get_aweme_token(url):
    timestamp = time.time()
    token_url = "http://132.232.61.103:4570/getascpmasb3989b15224a448791348c450a3ee915"
    parse_param = parse_qs(urlparse(url).query, keep_blank_values=True)
    data = {key: value[-1] for key, value in parse_param.items()}
    data.pop("mas")
    data.pop("cp")
    data.pop("as")
    data["_rticket"] = str(round(timestamp * 1000))
    data["ts"] = str(int(timestamp))
    ts_short = (str(int(timestamp)) + "504c53f18b834e8b9b853cc64628cd12").encode()
    param = {"dic": data, "device_id": data["device_id"], "ts_short": int(timestamp),
             "mykey": hashlib.md5(ts_short).hexdigest()}
    token = requests.post(token_url, data=json.dumps(param)).json()
    data["as"] = token["As"]
    data["mas"] = token["Mas"]
    data["cp"] = token["Cp"]
    return url.split("?")[0] + "?" + urlencode(data)


if __name__ in "__main__":
    # url = "https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=92941097220&max_time=1541660240&count=20&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=ALP-AL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=1024*576&dpi=192&update_version_code=1832&_rticket=1536744989405&ts=1536744990&as=a1a5dde97e81fbfea84355&cp=d31aba58ec819ee6e1McUg&mas=00a8422d39d7eb28de04f7adaffd1292f0acaccc2c1c86a6664666"
    # url = "https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=57015440195&max_time=1541500352&count=20&retry_type=no_retry&iid=49294240184&device_id=57259297041&ac=wifi&channel=wandoujia_zhiwei&aid=1128&app_name=aweme&version_code=310&version_name=3.1.0&device_platform=android&ssmix=a&device_type=BLA-AL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=310&resolution=576%2A1024&dpi=192&update_version_code=3102&_rticket=1541500371537&ts=1541500371&js_sdk_version=1.2.2&as=a155b60e530d6b8d814355&mas=00024cee3b307f2058632e8d193693a91aacaccc2c8c1c261c466c&cp=6ed4bf573e16eddce1aqKa"
    url = "https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=59126946917&max_time=1536762936&count=20&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=ALP-AL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=1024%2A576&dpi=192&update_version_code=1832&_rticket=1542013471523&ts=1542013471&as=a1c504beffd12b12594355&mas=002c9b6ee88d500a0a14bae3cb379eca5aacaccc2c9cac4c8c464c&cp=4913b95efd9aea29e1%5DaKa"
    print(get_aweme_token(url))
