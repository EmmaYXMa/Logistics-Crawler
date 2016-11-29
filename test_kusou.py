# -*- coding: UTF-8 -*- 
import sys
import requests
from bs4 import BeautifulSoup
import re
from urlparse import urlparse
from urlparse import urljoin
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://www.bjkufang.cn/kusou.aspx'
r = requests.get(url)

soup = BeautifulSoup(r.text)

g_data = soup.find_all('div',{'class':'btnr'})
for links in g_data:
    for link in links.findAll('a',{'target':'_blank'}): 
        href = urlparse.urljoin(url,link.get('href'))
    


'''
    try:
        print item.contents[1].find_all('li','class':'primary'})[0].text
    except:
        pass
'''


