# -*- coding: UTF-8 -*-  
import sys
import requests
from bs4 import BeautifulSoup
import re
reload(sys)
sys.setdefaultencoding('utf8')

def lease_spider(max_pages):
    page = 2
    while page <= max_pages:
        url = 'http://cangzhou.58.com/cangkucf/pn' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class': 't'}):
            href = link.get('href')
            #title = link.string
        
           # print href
           # print title
            get_single_item_data(href)
        page += 1
    print page

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    #plain_text = plain_text.replace(' ','_')    #将空格转化为下划线
    #plain_text = plain_text.replace('\n ','_')    #将空格转化为下划线
    soup = BeautifulSoup(plain_text) 
    for name in soup.findAll('h1', {'style':'font-size:22px;'}):
        item_name = name.string
    #for publish_info in soup.findAll('div',{'class':'other'}):
     #   publish_info_text = publish_info.get_text()
       # publish_time = re.search(u'发表时间：.*',publish_info_text)
       # if publish_time:
        #    time = publish_time.group()
       # else:
        #    time = str(None)
       # print publish_info_text
    f = open('58lease_warehouse_info_cangzhou.txt','a')
    
    #index = 1
    
    for item_info in soup.findAll('ul', {'class':'info'}):
        item_info_text = item_info.get_text() 
        igl = re.search(u"区域：.*",item_info_text)
        if igl:
            item_general_location = igl.group() #获取区域
        else:
            item_general_location = str(None)

        isl = re.search(u"地段：.*",item_info_text)
        if isl: 
            item_specific_location = isl.group()
        else: 
            item_specific_location = str(None) #获取地段
        
        area = re.search(u"面积：.*",item_info_text) #获取面积
        if area:
            item_area = area.group()
        else:
            item_area = str(None)

        x = re.search(u"租金：.*",item_info_text,re.S) #租金匹配 
        if x:
            item_lease_fee = x.group() #获取租金
        else:
            item_lease_fee = str(None)

        strings = u"河北" +',' + u"沧州" + ','+ item_name +',' +item_general_location + ',' + item_specific_location +',' + item_area + ',' + item_lease_fee
        s = re.sub('\s','',strings)
        string = re.sub (u"轻松买铺，贷来财富", '', s)
        
        f.write(string)
        f.write('\r\n')
        #index = index + 1
    f.close()
    
    h,r,w ={}, file('58lease_warehouse_info_cangzhou.txt'), file('58lease_warehouse_info_after_removral_cangzhou.txt','w')
    w.write(reduce(lambda x,y:x+y, [i for i in r if h.get(i)==None and h.setdefault(i, True)]))
#去除重复行
    
lease_spider(70) #设定爬虫页数
