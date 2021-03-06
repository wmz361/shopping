# -*- coding: utf-8 -*-
import random

__author__ = 'bliss'

from urllib import request
from urllib.parse import quote
from http.client import HTTPSConnection
from flask import json, current_app
import requests
from myapp.libs.proxy_ip import get_ip_list, get_random_ip

class HTTP:
    # 经典类和新式类
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

class Http(object):
    def __init__(self, url):
        self.url = url

    @staticmethod
    def get(url, json_return=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if json_return else ''
        return r.json() if json_return else r.text

    @staticmethod
    def get_with_request(url, json_return=True):
        url = quote(url, safe='/:?=&')
        # req = request.Request(url, headers=headers)
        try:
            with request.urlopen(url) as r:
                result_str = r.read()
                result_str = str(result_str, encoding='utf-8')
            if json_return:
                return json.loads(result_str)
            else:
                return result_str
        except OSError as e:
            # 对于外部的数据，如果出现异常，最好不要抛出来，而是应该默认值处理
            print(e.reason)
            if json_return:
                return {}
            else:
                return None

    def get_with_proxy(self, json_return=True):
        """
            使用代理ip访问
        """
        proxy_api_url = current_app.config['PROXY_API']
        url = quote(self.url, safe='/:?=&')
        result_str = None
        try:
            one_ip = self.get(proxy_api_url, json_return=False)
            one_ip = 'https://' + one_ip
            ua = random.choice(user_agent_list)
            proxy = {'https': one_ip}
            headers = {'User-Agent': ua}
            cookies = dict(bid=generate_app())
            data = requests.get(url, proxies=proxy, headers=headers, cookies=cookies)
            result_str = str(data.content, encoding='utf-8')
        except OSError as e:
            print(e.reason)
        if json_return:
            return json.loads(result_str)
        else:
            return result_str

    def post(self, host, url, data, headers=None):
        url = url.encode(encoding='utf-8')
        tmp_data = json.dumps(data)
        tmp_data = tmp_data.encode(encoding='utf-8')
        con = HTTPSConnection(host)
        con.request("POST", url, body=tmp_data, headers=headers)
        r = con.getresponse()
        # res = r.read()
        return r


user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]


def generate_app():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(11):
        sa.append(random.choice(seed))

    salt = ''.join(sa)
    return salt
