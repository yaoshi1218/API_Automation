# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 13:44
# @File    : test_invest.py
from test_case import *


@ddt
class Test_Invest(unittest.TestCase):  # 投资模块
    log = MyLog()
    http = HttpRequest()
    wb = DoExcel(test_case_path, 'invest')
    cases = wb.read_excel()

    # 读取invest表单文件
    def setUp(self):
        self.log.info('******开始执行******')

    def tearDown(self):
        self.log.info('******执行结束******')

    @data(*cases)
    def test_case(self, case):
        # 投资
        method = case['method']
        url = getattr(get_data.GetData,'url')+case['url']
        module = case['module']
        title = case['title']
        case_id = case['case_id']
        expected_result = case['expected_result']
        params = eval(get_data.replace(case['params']))  # 将手机号码和密码,用户id等替换进去

        if case_id == 1:  # 登录用例
            sql = get_data.replace(eval(case['sql'])['sql'])
            user_id = DoMySQL().do_mysql(sql)  # 拿到最新的user_id
            setattr(get_data.GetData, 'user_id', user_id[0])  # 将user_id存起来

        elif module == 'invest' and case['sql'] != None:
            sql=get_data.replace(eval(case['sql'])['sql'])
            # 取出投资前后的余额
            befor_amount = DoMySQL().do_mysql(sql)[0]
        # 返回实际的结果
        resp = self.http.http_request(method, url, params, cookies=getattr(get_data.GetData, 'COOKIE'))
        self.log.info('正在执行投资模块 {}，第{}条用例'.format(title, case_id))
        if case['module'] == 'invest' and case['sql'] != None:
            sql=get_data.replace(eval(case['sql'])['sql'])
            # 取出投资后的余额
            after_amount = DoMySQL().do_mysql(sql)[0]

        self.log.info('预期结果{}'.format(expected_result))
        self.log.info('实际结果{}'.format(resp.json()))
        if resp.cookies:
            setattr(get_data.GetData, 'COOKIE', resp.cookies)  # 设置cookies
        TestResult = None
        try:
            self.assertEqual(resp.json(), eval(expected_result))  # 进行断言比对
            if case_id == 2:
                invest_amount = int(params['amount'])  # 投资金额
                self.assertEqual(befor_amount-invest_amount, after_amount)  # 投资前后对比

            TestResult = 'Pass'
        except AssertionError as e:
            self.log.error('断言出错{}'.format(e))
            self.log.info(params)
            TestResult = 'Falsed'
            raise e
        finally:
            self.wb.write_excel(case['case_id'] + 1, 9, resp.text)  # 写入实际结果

            self.wb.write_excel(case['case_id'] + 1, 10, TestResult)  # 写入通过与未通过


if __name__ == '__main__':
    unittest.main()  # 自动加载test开头的数据
