# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 16:31
# @File    : test_register.py
from test_case import *


@ddt
class Test_Register(unittest.TestCase):  # 注册模块
    log = MyLog()
    http = HttpRequest()
    wb = DoExcel(test_case_path, 'register')
    cases = wb.read_excel()
    # 读取register表单文件

    def setUp(self):
        self.log.info('******开始执行******')

    def tearDown(self):
        self.log.info('******执行结束******')

    @data(*cases)
    def test_case(self, case):
        # 注册
        method = case['method']
        url = getattr(get_data.GetData, 'url') + case['url']
        params = case['params']
        title = case['title']
        case_id = case['case_id']
        expected_result = case['expected_result']

        resp = self.http.http_request(method, url, eval(params))  # 返回实际的结果
        self.log.info('正在执行注册模块 {}，第{}条用例'.format(title, case_id))
        self.log.info('预期结果{}'.format(expected_result))
        self.log.info('实际结果{}'.format(resp.json()))
        TestResult = None
        try:
            self.assertEqual(resp.json(), eval(expected_result))  # 进行断言比对
            TestResult = 'Pass'
            self.log.info('用例通过')
        except AssertionError as e:
            self.log.error('断言出错{}'.format(e))
            self.log.info(params)
            TestResult = 'Falsed'
            raise e
        finally:
            self.wb.write_excel(case_id + 1, 9, resp.text)  # 写入实际结果

            self.wb.write_excel(case_id + 1, 10, TestResult)  # 写入通过与未通过


if __name__ == '__main__':
    unittest.main()  # 自动加载test开头的数据
