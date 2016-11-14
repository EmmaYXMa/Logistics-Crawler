#coding=utf-8
import sys
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
r = requests.get('http://html-color-codes.info/color-names/')
html = r.text
soup = BeautifulSoup(html,'html.parser')
trs = soup.find_all('tr') 
f = open('color.txt','a')
index = 1
for tr in trs:
    style = tr.get('style')
    tds = tr.find_all('td')
    td = [ x for x in tds]
    name = td[1].text.strip()
    hex = td[2].text.strip()
    string = str(index) + ',' + name + ',' + hex + ',' + style
    f.write(string)
    f.write('\r\n')
    index = index +1
f.close()


