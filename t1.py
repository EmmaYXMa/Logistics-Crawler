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
        url = 'http://bj.58.com/cangkucf/pn' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class': 't'}):
            href = link.get('href')
            print href
         
        #print soup.find_all('class')
        page += 1

lease_spider(3) #设定爬虫页数




