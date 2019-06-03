# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 13:41
# @File    : test_add_loan.py
from Python接口项目实战.InterfaceTest.test_case import *
@ddt
class Test_Add_Loan(unittest.TestCase):#加标模块
    log=MyLog()
    http=HttpRequest()
    wb=DoExcel(test_case_path,'add_loan')
    cases=wb.read_excel()
    #读取add_loan表单文件
    def setUp(self):
        self.log.info('******开始执行******')

    def tearDown(self):
        self.log.info('******执行结束******')
    @data(*cases)
    def test_case(self,case):
        #加标
        method=case['method']
        module = case['module']
        url=getattr(get_data.GetData,'url')+case['url']
        title=case['title']
        case_id=case['case_id']
        expected_result=case['expected_result']

        params=eval(get_data.replace(case['params']))# 将手机号码和密码,用户id等替换进去
        if case_id==1:
            sql=get_data.replace(eval(case['sql'])['sql'])
            user_id = DoMySQL().do_mysql(sql)  # 拿到最新的user_id
            setattr(get_data.GetData, 'user_id', user_id[0])  # 将user_id存起来
        self.log.info('正在执行加标模块 {}，第{}条用例'.format(title, case_id))
        resp = self.http.http_request(method, url,params,cookies=getattr(get_data.GetData,'COOKIE'))  # 返回实际的结果
        if case_id==2:
            # 替换user_id为具体值
            sql=get_data.replace(eval(case['sql'])['sql'])
            loan_id=DoMySQL().do_mysql(sql)#拿到最新的loanid
            setattr(get_data.GetData,'loan_id',loan_id[0])#将loanid值存起来

        self.log.info('预期结果{}'.format(expected_result))
        self.log.info('实际结果{}'.format(resp.json()))
        if resp.cookies:
            setattr(get_data.GetData,'COOKIE',resp.cookies)#设置cookies

        TestResult=None
        try:
            self.assertEqual(resp.json(),eval(expected_result))#进行断言比对
            TestResult ='Pass'
        except AssertionError as e:
            self.log.error('断言出错{}'.format(e))
            self.log.info(str(params))
            TestResult = 'Falsed'
            raise e
        finally:
            self.wb.write_excel(case['case_id'] + 1, 9, resp.text)#写入实际结果

            self.wb.write_excel(case['case_id'] + 1, 10, TestResult)#写入通过与未通过




if __name__ == '__main__':
    unittest.main()#自动加载test开头的数据