#coding=UTF-8
import urllib2
from bs4 import BeautifulSoup
import os
num=1
#伪造浏览器标识,没有这个铁定不行，根据论坛的不同，甚至需要携带cookie 
header={
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:8.0.1) Gecko/20100101 Firefox/8.0.1'} 
#定义一个抓取函数，这个可以用于网页、图片的内容读取
def getsite(url):
    req=urllib2.Request(url,None,header)
    site=urllib2.urlopen(req)
    return site.read()
#循环，这个是页码范围，手工得到的
for i in xrange(1,38):
    print(i)
    try:
    first_url="http://pic.yesky.com/367/39732367d_%d.shtml"%i
    data=getsite(first_url)
    soup=BeautifulSoup(data)
    #用bs4解析，<th>标签内的<a>标签有个href就是每一个帖子的路径
    result=soup.find_all('th')
    for p in result:
        if p.find('a')>=0:
            a_url=p.find('a')
        else:
            continue
        try:
            second_url=a_url['href']
            print second_url

            twosite=getsite(second_url)
            #再找到帖子里的img标签
            toparse=BeautifulSoup(twosite)
            allpic=toparse.find_all('img')
            for q in allpic:
#两种情况
#一种图片网址可能在src属性里
                if q.get('src')!=None:
#下面这个规则是做筛选的，屏蔽了一些表情的东西
                    if q['src'].find('http')>=0:
                        picpath=q['src']
                        print picpath
                        picname="result/%d.jpg"%num
                        pic=open(picname,'wb')
                        pic.write(getsite(picpath))
                        pic.close()
                        #如果图片大小小于10kb就删除
                        if os.path.getsize(picname)<10240:
                            os.remove(picname)
                        else:
                            num+=1

                #一种图片网址可能在file属性里
                if q.get('file')!=None:
                    #下面这个规则是做筛选的
                    if q['file'].find('data/')>=0:
                        picpath='你的论坛地址'+q['file']
                        print picpath
                        picname="result/%d.jpg"%num
                        pic=open(picname,'wb')
                        pic.write(getsite(picpath))
                        pic.close()
                        #如果图片大小小于10kb就删除
                        if os.path.getsize(picname)<10240:
                            os.remove(picname)
                        else:
                            num+=1


except (IOError,TypeError),e:
    print "IO:%s"%e
except KeyError,e:
    print "Key not find:%s"%e