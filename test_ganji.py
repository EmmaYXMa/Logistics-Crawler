import sys
import requests
from bs4 import BeautifulSoup
import re
reload(sys)
sys.setdefaultencoding('utf8')

def lease_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://bj.ganji.com/fang11/h10' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class': 'list-title'}):
            href = link.get('href')
            print href

lease_spider(1)
