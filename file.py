#!/usr/bin/env python3
#coding:utf-8
''' @time = '2018年10月22日 17:44' '''

# 写入文件
fe = open('douban.txt','w',encoding='utf-8')
fe.write(str(now_movie_list))
fe.close()