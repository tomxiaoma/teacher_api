"""
# author:xiaoma
# datetime:2019/10/22 11:44
describe:涵盖http的请求方式
"""
import requests
import json
from config.loggingReader import *


class RunMethod:
    def get_method(self,url,header,data=None):
        """
        封装get请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header ==None:
            res = requests.get(url=url,data=data).json()
        else:
            res = requests.get(url=url,data=data,header=header).json()
        return res

    def post_method(self,url,data,header=None):
        """
        封装post请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header ==None:
            res = requests.post(url=url,data=data).json()
        else:
            res = requests.post(url=url,data=data,header=header).json()
        return res

    def put_method(self,url,data,header=None):
        """
        封装put方法
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header ==None:
            res = requests.post(url=url,data=data).json()
        else:
            res = requests.post(url=url,data=data,header=header).json()
        return res

    def delete_method(self,url,data,header=None):
        """
        封装delete方法
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if header == None:
            res = requests.post(url=url,data=data).json()
        else:
            res = requests.post(url=url,data=data,header=header).json()
        return res

    def run_main(self,method,url,data=None,header=None):
        """
        封装一个执行入口
        :param method:
        :param url:
        :param data:
        :param header:
        :return:
        """
        res = None
        if method == 'post':
            res = self.post_method(url=url,data=data,header=header)
        elif method == 'get':
            res = self.get_method(url=url,data=data,header=header)
        elif method == 'put':
            res = self.put_method(url=url, data=data, header=header)
        elif method == 'delete':
            res = self.delete_method(url=url, data=data, header=header)
        else:
            logging.error("暂时不支持其他请求方式")
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
