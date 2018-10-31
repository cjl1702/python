#!/usr/bin/env python3
#coding:utf-8
#date 2018/10/31

import urllib.request
from bs4 import BeautifulSoup as bs
import jieba #分词包
import pandas as  pd


# 评论请求地址
url = 'https://movie.douban.com/subject/26363254/comments?start=0&limit=20'
request = urllib.request.Request(url)

# 爬取结果
response = urllib.request.urlopen(request)
data = response.read()

# 设置解码方式
html_data = data.decode('utf8')


# beautifulSoup解析html  推荐lxml和html5lib方式解析
soup = bs(html_data,'html.parser')
now_comment = soup.find_all("div",class_='comment')

#解析获取评论内容
content = ''
for comment_data in now_comment:
    new_comment_dict = {}
    comments = comment_data.find_all("span",class_="short")
    for comment in comments:
        #获取标签内的内容
        content += comment.string.strip()


#清洗数据，去掉标签符号
segment = jieba.lcut(content)
words_df=pd.DataFrame({'segment':segment})



fe = open('comment.txt','w',encoding='utf-8')
fe.write(str(words_df))
fe.close()

print(html_data)
exit()
