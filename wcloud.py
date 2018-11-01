#!/usr/bin/env python3
#coding:utf-8
#date 2018/10/31

import urllib.request
from bs4 import BeautifulSoup as bs
import jieba #分词包
import pandas as  pd # 结巴分词 需要用到pandas包，做数据清理
import numpy

# 评论请求地址
url = 'https://movie.douban.com/subject/26363254/comments?start=0&limit=20'
request = urllib.request.Request(url)

# 爬取结果
response = urllib.request.urlopen(request)
data = response.read()

# 设置解码方式
html_data = data.decode('utf-8')


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

# 清洗数据,得出高频词语
segment = jieba.lcut(content)
words_df=pd.DataFrame({'segment':segment})


# 与停用词对比，去掉虚词
# quoting = 3 全不引用
stopwords = pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="t",names=['stopword'],encoding='gb18030')
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]


# 进行词频统计
words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"],ascending=False)
print(words_stat.head())


# 用词云展示
import matplotlib.pyplot as plt
#%matplotlib inline
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud#词云包
wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80) #指定字体类型、字体大小和字体颜色
word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

word_frequence_list1 = []
word_frequence_list2 = []
for key in word_frequence:
    #temp = (key,word_frequence[key])
    word_frequence_list1.append(key)
    word_frequence_list2.append(word_frequence[key])

# word_dict
word_dict = zip(word_frequence_list1, word_frequence_list2)
word_dict = dict((name, value) for name, value in word_dict)

wordcloud = wordcloud.fit_words(word_dict)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()



fe = open('comment.txt','w',encoding='utf-8')
fe.write(str(words_df))
fe.close()

#print(html_data)
#exit()
