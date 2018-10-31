#!/usr/bin/env python3
#coding:utf-8
''' @time = '2018年10月22日 17:44' '''

import time
import pymysql
import urllib.request
from bs4 import BeautifulSoup as bs



# 请求
url = "https://movie.douban.com/nowplaying/hangzhou"
request = urllib.request.Request(url)


# 爬取结果
response = urllib.request.urlopen(request)
data = response.read()

# 设置解码方式
html_data = data.decode('utf8')



# beautifulSoup解析html  安装：pip install beautifulsoup4
soup = bs(html_data,'html.parser')
now_movie = soup.find_all("div",id='nowplaying')

now_movie_list = now_movie[0].find_all('li',class_='list-item')
# print(now_movie_list[0])

# 清洗数据
new_data = []

for item_info in now_movie_list:
    new_data_dict = {}
    new_data_dict['id'] = item_info['data-subject']
    new_data_dict['actors'] = item_info['data-actors']

    #获取img信息
    item_info = item_info.find_all('img')
    for item in item_info:
        new_data_dict['name'] = item['alt']
        new_data_dict['img']  = item['src']

        new_data.append(new_data_dict)
# 操作数据库
db = pymysql.connect("localhost","root","root","pythoncjl")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQl操作语句
sql = 'insert into film values '
for key,data in enumerate(new_data):
    # 不同变量类型不能进行拼接
    current_time = str(time.time())
    sql += "(" + data['id'] + ",'" + data['name'] + "','" + data['actors'] + "','" + data[
        'img'] + "'," + current_time + ")"
    # 判断最后一条数据不加'逗号'
    if key != len(new_data)-1:
        sql += ","

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    db.rollback()
    print('插入失败，进行回滚')

# 关闭数据库
db.close()
