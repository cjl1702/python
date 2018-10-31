#!/usr/bin/env python3
#coding:utf-8
''' @time = '2018年10月22日 17:44' '''

import pymysql
import urllib.request
from bs4 import BeautifulSoup as bs


# 操作数据库
db = pymysql.connect("localhost","root","root","pythoncjl")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQl操作语句
sql = "select * from film"
cursor.execute(sql)

results = cursor.fetchall()
print(results)


# 设置解码格式
# print(html_data)