# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 7:52
# @File    : do_mysql.py
from mysql import connector
from common.public.project_path import *
from common.public.my_config import ReadConfig
import datetime


class DoMySQL:

    def do_mysql(self, query, flag=1):
        """操作数据的类
        query sql查询语句
        flag 标志 1 获取一条数据 2获取多条数据"""
        db = ReadConfig(conf_path).read_other('MySQL', 'db')  # 读取配置文件
        cnn = connector.connect(**db)   # 链接数据库

        cursor = cnn.cursor()  # 获取游标，获得数据库权限

        cursor.execute(query)  # 获取sql语句

        if flag == 1:
            res = cursor.fetchone()
            cursor.close()
        else:
            res = cursor.fetchall()
            cursor.close()
        return res


if __name__ == '__main__':
    query = 'select * from member where MobilePhone=13677885645'
    res = DoMySQL().do_mysql(query, 1)
    # data = {}
    # data['时间'] = res.strftime("%Y-%m-%d %H:%M:%S.0")
    print(res)
