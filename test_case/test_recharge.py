# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 8:40
# @File    : test_recharge.py

from test_case.get_data import GetData
from test_case import *


@ddt
class Test_Recharge(unittest.TestCase):  # 充值模块
    log = MyLog()
    http = HttpRequest()
    wb = DoExcel(test_case_path, 'recharge')
    cases=wb.read_excel()
    # 读取recharge表单文件

    def setUp(self):
        self.log.info('******开始执行******')

    def tearDown(self):
        self.log.info('******执行结束******')

    @data(*cases)
    def test_case(self, case):
        # 充值
        method = case['method']
        url = getattr(get_data.GetData, 'url')+case['url']
        params = case['params']
        title = case['title']
        case_id = case['case_id']
        expected_result = case['expected_result']
        p = '#(.*?)#'  # 匹配规则
        if case_id == 2:
            sql = eval(case['sql'])['sql_amount']  # 取出SQL语句
            befor_amount = float(DoMySQL().do_mysql(sql)[0])  # 充值之前的余额
        self.log.info('正在执行充值模块 {}，第{}条用例'.format(title, case_id))
        # 返回实际的结果
        resp = self.http.http_request(method, url,eval(params), cookies=getattr(GetData, 'COOKIE'))
        if case_id == 2:
            values = DoMySQL().do_mysql(eval(case['sql'])['sql_data'])[:7]  # 判断sql不为空，取出断言所需内容
            print(values)
            data = {}
            # 将values内容加入到data中
            data['id'] = values[0]
            data['regname'] = values[1]
            data['pwd'] = values[2]
            data['mobilephone'] = values[3]
            data['type'] = str(values[4])
            recharge_amount = float(eval(params)['amount'])  # 充值金额
            data['leaveamount'] = str(befor_amount + recharge_amount)  # 期望值余额

            after_amount = float(values[5])  # 充值后的余额
            data['regtime'] = values[6].strftime("%Y-%m-%d %H:%M:%S.0")
            # 用正则替换进去，生成新的预期结果

            expected_result = re.sub(p, str(data), case['expected_result'])

        self.log.info('预期结果{}'.format(expected_result))
        self.log.info('实际结果{}'.format(resp.json()))
        if resp.cookies:
            setattr(GetData,'COOKIE', resp.cookies)  # 设置cookies
        TestResult = None
        try:
            self.assertEqual(resp.json(), eval(expected_result))  # 进行断言比对
            if case_id == 2:
                self.assertEqual(befor_amount + recharge_amount, after_amount)  # 金额做对比
            TestResult = 'Pass'
        except AssertionError as e:
            self.log.error('断言出错{}'.format(e))
            TestResult = 'Falsed'
            raise e
        finally:
            self.wb.write_excel(case['case_id'] + 1, 9, resp.text)  # 写入实际结果

            self.wb.write_excel(case['case_id'] + 1, 10, TestResult)  # 写入通过与未通过


if __name__ == '__main__':
    unittest.main()  # 自动加载test开头的数据

