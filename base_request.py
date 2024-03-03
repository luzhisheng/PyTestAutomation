import json

import requests
from Util.handle_init import handle_init
from Util.handle_json import read_json


class BaseRequest(object):

    def send_post(self, url, data):
        '''
        发送post请求
        :param url:
        :param data:
        :return:
        '''
        res = requests.post(url=url, data=data).text
        return res

    def send_get(self, url, data):
        '''
        发送get请求
        :param url:
        :param data:
        :return:
        '''
        res = requests.get(url=url, params=data).text
        return res

    def run_main(self, method, url, data):
        '''
        执行方法，传递method、url、data参数
        :param method:
        :param url:
        :param data:
        :return:
        '''

        base_url = handle_init.get_value('host')

        if 'http' not in url:
            url = base_url + url

        if method == "get":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        try:
            res = json.loads(res)
        except:
            print("结果是个text")
        return res


request = BaseRequest()


if __name__ == '__main__':
    request = BaseRequest()
    request.run_main('get', 'login/', "{'username': 111111}")
