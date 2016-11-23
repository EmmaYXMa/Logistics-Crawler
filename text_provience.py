# -*- coding: UTF-8 -*-  
import sys
import requests
from bs4 import BeautifulSoup
import re
reload(sys)
sys.setdefaultencoding('utf8')

#def lease_spider(provience,max_pages):
nation_url = 'http://www.58.com/cangkucf/changecity/'
source_code = requests.get(nation_url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text)
#print soup
for link in soup.findAll('dl', {'id':'clist'}): 
    href = link.get('href')
    print link

