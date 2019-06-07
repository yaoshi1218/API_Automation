# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 17:17
# @File    : main.py

from HTMLTestRunnerNew import HTMLTestRunner
from common.public.project_path import *
from common.public.my_config import ReadConfig
from test_case.test_login import Test_Login
from test_case.test_recharge import Test_Recharge
from test_case.test_register import Test_Register
from test_case.test_withdraw import Test_Withdraw
from test_case.test_add_loan import Test_Add_Loan
from test_case.test_invest import Test_Invest
import unittest
suite = unittest.TestSuite()
loader = unittest.TestLoader()
config = ReadConfig(conf_path)  # 配置文件类实例
module_name = config.read_str('MODULE', 'module_name')  # 读取配置文件，选择要读取的模块

if module_name == 'all':
    suite.addTests(loader.loadTestsFromTestCase(Test_Register))  # 加载测试用例类
    suite.addTests(loader.loadTestsFromTestCase(Test_Login))  # 加载测试用例类
    suite.addTests(loader.loadTestsFromTestCase(Test_Withdraw))  # 加载测试用例类
    suite.addTests(loader.loadTestsFromTestCase(Test_Recharge))  # 加载测试用例类
    suite.addTests(loader.loadTestsFromTestCase(Test_Add_Loan))
    suite.addTests(loader.loadTestsFromTestCase(Test_Invest))
else:
    for module in eval(module_name):
        suite.addTests(loader.loadTestsFromTestCase(module))
mkdir(test_report)
with open(test_report+'\\test_report.html', 'wb')as file:
    runner = HTMLTestRunner(stream=file,verbosity=2,
                            title='接口测试报告', description='接口报告')
    runner.run(suite)   # 执行用例的类

