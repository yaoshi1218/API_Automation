# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 8:41
# @File    : get_data.py
from Python接口项目实战.InterfaceTest.test_case import *
import re
class GetData:
    '''可以用来动态的更改、删除
    获取数据'''
    COOKIE=None
    LOAN_ID=None#标id
    user_id=None#用户id
    PHONE = '18688775656'
    PWD = '123456'
    #用户的登录的账号和密码
    normal_user=ReadConfig(conf_path).read_str('DATA','normal_user')
    normal_pwd=ReadConfig(conf_path).read_str('DATA','normal_pwd')
    url=ReadConfig(conf_path).read_str('URL','url')


def replace(target):
    p = '#(.*?)#'  # 匹配规则
    while re.search(p,target):#是否有要替换的字段
        m=re.search(p,target)
        key=m.group(1)#得到要替换的字段
        value=getattr(GetData,key)#拿到替换进去的值
        target=re.sub(p,str(value),target,count=1)#进行替换
    return target



if __name__=='__main__':
    # print(hasattr(GetData,'COOKIE'))
    # setattr(GetData,'TEL',123)

    # delattr(GetData,'COOKIE')
    # print(getattr(GetData, 'COOKIE'))
    a="{'mobilephone': #normal_user#,'pwd':#normal_pwd#}"
    print(replace(a))



