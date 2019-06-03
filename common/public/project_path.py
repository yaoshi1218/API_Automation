# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 8:50
# @File    : project_path.py
import os
project_path = os.path.realpath(__file__)#获取当前文件目录
#common目录下 文件夹地址
common_path = os.path.split(os.path.split(project_path)[0])[0]#获取common文件夹路径
conf_path = os.path.join(common_path,'conf','config.ini')#获得conf 文件夹路径
conf_new_path = os.path.join(common_path,'conf','config_new.ini')#获得conf 文件夹路径



interfaceTest_path = os.path.split(common_path)[0]#获取interfaceTest 文件夹路径
#result文件夹下目录的地址
test_log_path = os.path.join(interfaceTest_path,'result','test_log')#获取test_log文件夹路径
test_report = os.path.join(interfaceTest_path,'result','test_report')#获取test_report文件夹路径

test_data_path = os.path.join(interfaceTest_path,'test_data')#获取test_data文件夹路径
test_case_path=os.path.join(test_data_path,'test_case.xlsx')
if __name__=='__main__':
    print(project_path)
    print(common_path)
    print(test_log_path)
    print(interfaceTest_path)