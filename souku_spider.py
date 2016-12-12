#encoding:utf-8

import os
import time
import urllib
import codecs
import urllib2
from bs4 import BeautifulSoup


domain = "http://www.bjkufang.cn"
def get_pages():
    url = domain + "/kusou.aspx"
    for i in range(5, 10):
        time.sleep(10)
        page = i+1  #从第6页爬到第11页
        print page
        data = "__EVENTARGUMENT=" + str(page) + "&__EVENTTARGET=AspNetPager1"
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        content = response.read().decode('gb2312', 'ignore')
        soup = BeautifulSoup(content.encode("utf-8"))
        f = codecs.open('pages/page%d' % page, 'w', "utf-8") #把page写入文档中
        f.write(content)
        f.close()


def parse_page(page):
    urls = []
    f = codecs.open('pages/page%d' % page, 'r', "utf-8")
    soup = BeautifulSoup(f.read())
    for h1 in soup.findAll('h1'):
        url = h1.a['href']
        urls.append(url)
        print url
    f.close()

    for url in urls:
        full_url = domain + '/' + url
        time.sleep(2)
        response = urllib2.urlopen(full_url)
        content = response.read().decode('gb2312', 'ignore')
        soup = BeautifulSoup(content.encode("utf-8"))
        f = codecs.open('/Users/apple/Documents/Logistics-Web-Crawler/souku_bj%s' % url[19:], 'w', "utf-8")
        f.write(content)
        f.close()
        print url, 'fetched!'


def parse_labs():
    labs = os.listdir('/Users/apple/Documents/Logistics-Web-Crawler')
    keys = [u'名称：', u'描述：']
    lab_infos = []
    for lab in labs:
        f = codecs.open('/Users/apple/Documents/Logistics-Web-Crawler/souku_bj%s' % lab, 'r', "utf-8")
        content = f.read()
        soup = BeautifulSoup(content)
        f.close()
        name = soup.find('span', {'id': 'Labtitle'}).text.strip()
        desc = soup.find('div', {'class': 'jstextk'}).text.strip()
        info = {
            u'名称：': name,
            u'描述：': desc
        }
        #print 'name:', name
        #print 'desc:', desc

        details = soup.find('div', {'class': 'dc_fl'})
        details = details.findAll('li')
        for detail in details:
            spans = detail.findAll('span')
            if len(spans) >= 2:
                key, value = spans[0].text.strip(), spans[1].text.strip()
                #print key, value
                if key not in keys:
                    keys.append(key)
                info[key] = value
        lab_infos.append(info)
        #print
        #print

    #f = codecs.open('labs.txt' % lab, 'w', "utf-8")
    for info in lab_infos:
        for key in keys:
            if key in info.keys():
                line = u"%s%s" % (key, info[key])
                print line.encode('utf-8', 'ignore')
                #f.write(key.encode('utf-8'))
                #f.write(info[key].encode('utf-8'))
                #f.write('\n')
        print('\n\n')
    #1f.close()

if __name__ == "__main__":
    parse_labs()
