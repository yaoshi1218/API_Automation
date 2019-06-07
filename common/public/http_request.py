# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 8:53
# @File    : http_request.py
import requests


class HttpRequest:
    def __init__(self):
        """设置请求头"""
        # self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #                         'Chrome/51.0.2704.63 Safari/537.36'}

    def http_request(self,method, url, param=None, **kwargs):
        """执行请求method,请求的方式，url请求的网址，param传入的参数, response返回结果"""
        response = None
        if method.upper() == 'GET':
            try:
                response = requests.get(url, params=param, **kwargs)
            except Exception as e:
                raise e
        elif method.upper() == 'POST':
            try:
                response = requests.post(url, data=param, **kwargs)
            except Exception as e:
                raise e
        else:
            pass
        return response


if __name__=='__main__':
    http=HttpRequest()
    url='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    # url='https://www.baidu.com/'
    Params = {'mobilephone':'13677885696','pwd':'123456'}
    res=http.http_request('get',url,Params)
    print(res.text)
    print(res.cookies)
