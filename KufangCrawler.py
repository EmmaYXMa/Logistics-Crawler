#encoding:utf-8
import os
import time
import urllib
import codecs
import urllib2
from bs4 import BeautifulSoup

def KufangCrawler(start,end):
    directory="/Users/apple/Documents/Logistics-Web-Crawler/"
    domain = "http://www.bjkufang.cn"
    os.makedirs(directory+"result_"+str(start)+"_"+str(end)+"/pages")
    os.makedirs(directory+"result_"+str(start)+"_"+str(end)+"/labs")
    url=domain+"/kusou.aspx"
    for i in range(start,end):
        time.sleep(10)
        print i
        data = "__EVENTARGUMENT=" + str(i) + "&__EVENTTARGET=AspNetPager1"
        req=urllib2.Request(url,data)
        response=urllib2.urlopen(req)
        content = response.read().decode('gb2312', 'ignore')
        soup = BeautifulSoup(content.encode("utf-8"))
        f = codecs.open(directory+"result_"+str(start)+"_"+str(end)+"/pages/page%d" % i, 'w', "utf-8")
        f.write(content)
        f.close()
        
        urls=[]
        f = codecs.open(directory+"result_"+str(start)+"_"+str(end)+"/pages/page%d" % i, 'r', "utf-8")
        soup = BeautifulSoup(f.read())
        for h1 in soup.findAll('h1'):
            surl=h1.a['href']
            urls.append(surl)
            print surl
        f.close()

        for surl in urls:
            full_url = domain + '/' + surl
            time.sleep(2)
            response = urllib2.urlopen(full_url)
            content = response.read().decode('gb2312', 'ignore')
            soup = BeautifulSoup(content.encode("utf-8"))
            f = codecs.open(directory+'result_'+str(start)+"_"+str(end)+'/labs/lab_%s' % surl[19:], 'w', "utf-8")
            f.write(content)
            f.close()
            print url, 'fetched!'
    labs=os.listdir(directory+'result_'+str(start)+"_"+str(end)+'/labs')
    keys=[u'名称：', u'描述：']
    lab_infos = []
    for lab in labs:
        f = codecs.open('/Users/apple/Documents/Logistics-Web-Crawler/result_'+str(start)+"_"+str(end)+'/labs/%s' % lab, 'r', "utf-8")
        content = f.read()
        soup = BeautifulSoup(content)
        f.close()
        name = soup.find('span', {'id': 'Labtitle'}).text.strip()
        desc = soup.find('div', {'class': 'jstextk'}).text.strip()
        info = {
            u'名称：': name,
            u'描述：': desc
        }
        details = soup.find('div', {'class': 'dc_fl'})
        details = details.findAll('li')
        for detail in details:
            spans = detail.findAll('span')
            if len(spans) >= 2:
                key, value = spans[0].text.strip(), spans[1].text.strip()
                if key not in keys:
                    keys.append(key)
                info[key] = value
            lab_infos.append(info)

    file = codecs.open(directory+"result_"+str(start)+"_"+str(end)+"/CrawlResult", "w", "utf-8")
    for info in lab_infos:
        for key in keys:
            for key in info.keys():
                line = u"%s%s" % (key, info[key])
                file.write(line)
                file.write('\n')
            file.write('\n')
        file.write('\n\n')
    file.close()

