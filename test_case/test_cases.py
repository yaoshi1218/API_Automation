# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 17:56
# @File    : test_cases.py
import unittest
from my_ddt import ddt,data
from my_log import MyLog
from do_excel_new import DoExcel
from http_request import HttpRequest
from project_path import *
from get_data import GetData
log=MyLog()
http=HttpRequest()
cases=DoExcel(test_case_path).read_excel()
@ddt
class Test_All(unittest.TestCase):
    #读取表单文件
    def setUp(self):
        log.info('******开始执行******')
    def tearDown(self):
        log.info('******执行结束******')
    @data(*cases)
    def test_case(self,case):
        method=case['method']
        url=case['url']
        params=eval(case['params'])
        write=DoExcel(test_case_path)#创建写回实例

        resp = http.http_request(method,url,params,cookies=getattr(GetData,'COOKIE'))  # 返回实际的结果
        log.info('正在执行{}模块 {}，第{}条用例'.format(case['sheet_name'],case['title'],case['case_id']))
        log.info('预期结果{}'.format(case['expected_result']))
        log.info('实际结果{}'.format(resp.json()))
        if resp.cookies:
            setattr(GetData,'COOKIE',resp.cookies)#设置cookies
        TestResult=None
        try:
            self.assertEqual(resp.json(), eval(case['expected_result']))#进行断言比对
            TestResult = 'Pass'
            log.info('用例通过')
        except AssertionError as e:
            log.error('断言出错{}'.format(e))
            log.info(case['params'])
            TestResult = 'Falsed'
            raise e
        finally:
            write.write_excel(case['sheet_name'],case['case_id'] + 1, 8, resp.text)#写入实际结果

            write.write_excel(case['sheet_name'],case['case_id'] + 1, 9, TestResult)#写入通过与未通过


if __name__ == '__main__':
    unittest.main()#自动加载test开头的数据