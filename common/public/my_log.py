
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 9:08
# @File    : my_log.py
import logging,datetime
from common.public.my_config import ReadConfig
from common.public.project_path import *   # 引用test_log路径


class MyLog:
    config = ReadConfig(conf_path)  # 配置文件类实例

    format = config.read_str('My_Log', 'format')  # 输出格式
    my_logger = config.read_str('My_Log', 'my_logger')  # 日志收集器的名称
    my_logger_lv = config.read_str('My_Log', 'my_logger_lv')  # 日志收集器等级
    # log_file_name = config.read_str('My_Log', 'log_file_name')  # 日志文件名称
    log_file_name = datetime.datetime.now().strftime("%Y%m%d")+ '.log'  # 日志文件名称
    ch_lv = config.read_str('My_Log', 'ch_lv')  # 控制台输出等级
    fh_lv = config.read_str('My_Log', 'fh_lv')  # 文本输出等级
    '''这是一个日志类'''

    def my_log(self, level, msg):

        """level 设置输出日志等级
        msg 设置输出日志内容"""
        my_logger=logging.getLogger(self.my_logger)  # 设置日志收集器名称
        my_logger.setLevel(self.my_logger_lv)  # 设置日志收集器等级

        set_format = logging.Formatter(self.format)  # 设置日志输出格式

        ch=logging.StreamHandler()  # 设置输出到控制台
        ch.setLevel(self.ch_lv)  # 控制台设置输出日志等级
        ch.setFormatter(set_format)  # 控制台设置输出日志格式
        mkdir(test_log_path)
        fh = logging.FileHandler(test_log_path+'\\'+self.log_file_name, encoding='utf-8')  # 设置输出到文本
        fh.setLevel(self.fh_lv)  # 文本设置输出日志等级
        fh.setFormatter(set_format)  # 文本设置输出日志格式

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)  # 连接收集器和输出位置

        if level.upper() == 'DEBUG':  # 对level进行判断，输出对应等级日志信息
            my_logger.debug(msg)
        elif level.upper() == 'INFO':
            my_logger.info(msg)
        elif level.upper() == 'WARNING':
            my_logger.warning(msg)
        elif level.upper() == 'ERROR':
            my_logger.error(msg)
        else:                          # CRITICAL
            my_logger.critical(msg)

        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)  # 移除重复日志

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)


if __name__=='__main__':
    ml=MyLog()
    ml.info('要你管我')


