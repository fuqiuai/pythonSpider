# 爬取豆瓣top250电影及封面

import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import time
import os

def getImg(url,params,start):
    '''获取豆瓣top250电影及封面'''
    response=requests.get(url,params=params,timeout=10) 
    soup=BeautifulSoup(response.text,'lxml') 

    #保存电影封面至本地
    index=1+start
    try:
        for item in soup.find_all(class_='item'):
            imgUrl=item.find(class_='pic').a.img['src']
            info=item.find(class_='info').find(class_='bd').p.contents[2].strip()
            i=len(info.split('/'))-2
            country=info.split('/')[i].strip()
            if os.path.exists('douban_top250/')==False:
                os.mkdir('douban_top250/')
            imgName='douban_top250/top'+str(index)+' '+item.find(class_='pic').a.img['alt']+'('+country+')'+'.jpg'            
            urllib.request.urlretrieve(imgUrl,imgName)
            print('成功抓取',str(index),'张')    
            index+=1
            time.sleep(0.5) #睡眠函数用于防止爬去过快被封ip
    except:
        print("抓漏了1张")


url='https://movie.douban.com/top250'
for start in range(0,250,25):
    params={'start':start}
    getImg(url,params,start)

