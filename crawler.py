#coding:utf-8
''' @time = '2018年10月22日 17:44' '''

import urllib.request
from bs4 import BeautifulSoup as bs


#请求
url = "https://movie.douban.com/nowplaying/hangzhou"
request = urllib.request.Request(url)


#爬取结果
response = urllib.request.urlopen(request)
data = response.read()

#设置解码方式
html_data = data.decode('utf8')



#beautifulSoup解析html  安装：pip install beautifulsoup4
soup = bs(html_data,'html.parser')
now_movie = soup.find_all("div",id='nowplaying')

now_movie_list = now_movie[0].find_all('li',class_='list-item')
#print(now_movie_list[0])

#清洗数据
new_data = []
for item in now_movie_list:
    new_data_dict = {}
    new_data_dict['id'] = item['data-subject']

    print(type(new_data_dict))
    print(item['data-actors'])



#写入文件
fe = open('douban.txt','w',encoding='utf-8')
fe.write(str(now_movie_list))
fe.close()

#设置解码格式
#print(html_data)