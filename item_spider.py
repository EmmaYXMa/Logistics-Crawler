# -*- coding: UTF-8 -*-  
import requests
from bs4 import BeautifulSoup
import re

def lease_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://bj.58.com/cangkucf/pn' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class': 't'}):
            href = link.get('href')
            title = link.string
           # print href
           # print title
            get_single_item_data(href)
            page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('h1', {'style':'font-size:22px;'}):
        print (item_name.string)
    for item_info in soup.findAll('ul', {'class':'info'}):
        item_info_text = item_info.get_text()
        item_general_location = re.search(u"区域：.*",item_info_text).group()
        item_specific_location = re.search(u"地段：.*",item_info_text).group()
        item_area = re.search(u"面积：.*",item_info_text).group()
        item_lease_fee = re.search(u"租金：.*",item_info_text).group()
        print item_general_location
        print item_specific_location
        print item_area
    #for item_lease_fee in soup.findAll('em', {'class':'redfont'}):
        #print u"租金：" + (item_lease_fee.string)
        #print item_info_text
        print item_lease_fee

lease_spider(1)
