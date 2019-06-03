# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 15:49
# @File    : my_config.py
from configparser import ConfigParser
from Python接口项目实战.InterfaceTest.common.public.project_path import *
class ReadConfig:
    '''这是一个读取配置文件的类'''
    def __init__(self, file_name):
        '''file_name:要读取配置文件的名称'''
        self.cf = ConfigParser()  # 创建实例化对象
        self.file_name = file_name
        self.cf.read(self.file_name, encoding='utf-8')  # 读取文件设置编码格式

    def read_int(self, section, option):
        '''读取整数的方法
        section:配置文件的section,option:配置文件的option'''
        value = self.cf.getint(section, option)  # 进行读值
        return value

    def read_float(self, section, option):
        '''读取浮点数的方法
        section:配置文件的section,option:配置文件的option'''
        value = self.cf.getfloat(section, option)
        return value

    def read_bool(self, section, option):
        '''读取布尔值的方法
        section:配置文件的section,option:配置文件的option'''
        value = self.cf.getboolean(section, option)
        return value

    def read_str(self, section, option):
        '''读取字符串的方法
        section:配置文件的section,option:配置文件的option'''
        value = self.cf.get(section, option)
        return value

    def read_other(self, section, option):
        '''读取list，tuple，dict的方法
        section:配置文件的section,option:配置文件的option'''
        value = self.cf.get(section, option)
        return eval(value)

if __name__ == '__main__':
    config = ReadConfig(conf_path + '\\config.ini')  # 配置文件类实例
    read_row = config.read_str('Do_Excel', 'read_row')
    print(read_row)