from lxml import etree
import csv
import requests
import json
def get_page(url):
    headers = {
        'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    cookies = {
        'cookie':'bid="dDi4Ej8VlXw"; ll="118159"; __utmc=30149280; _vwo_uuid_v2=D598C964736D559B4D7D0F397D5D3970A|7b30a828dfd8ac5099cc76928e5bf247; __gads=ID=d08666ef0c486f08:T=1600437871:S=ALNI_Mb1ckWHCXnWqUaGt4WluOeyT7YFRw; __yadk_uid=EWypb2CJs37Tg6KZqoPFEQvzQhJa1Kfz; push_doumail_num=0; push_noty_num=0; __utmv=30149280.22363; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1600491788%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin_popup%3Flogin_source%3Danony%22%5D; _pk_id.100001.8cb4=f83ff8e7058502e7.1600439393.4.1600491799.1600489001.; __utma=30149280.71960709.1600437860.1600491774.1600505276.5; __utmb=30149280.0.10.1600505276; __utmz=30149280.1600505276.5.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; dbcl2="223635887:X5zmr7TfRso"; ck=kkp_'
    }
    response = requests.get(url=url,headers=headers,cookies=cookies)
    html = response.text
    return html

def getdata(url):
    html = get_page(url)
    Html = etree.HTML(html)
    comments=Html.xpath('//div[@class="short-content"]')
    author=Html.xpath('//a[@class="name"]/text()')
    time=Html.xpath('//span[@class="main-meta"]/text()')
    stars=Html.xpath('//header[@class="main-hd"]/span/@title')
    like=Html.xpath('//div[@class="action"]/a[1]/span')
    dislike = Html.xpath('//div[@class="action"]/a[2]/span')
    for i in range(0,len(comments)):
        comments[i]=comments[i].xpath('string(.)').strip()
        dislike[i]=dislike[i].xpath('string(.)').strip()
        like[i]=like[i].xpath('string(.)').strip()
    # print(len(comments),comments)
    # print(len(author),author)
    # print(len(time),time)
    # print(len(stars),stars)
    # print(len(like),like)
    # print(len(dislike),dislike)
    data = zip(author,time,stars,comments,like,dislike)
    return data;

def savefile(data):
    f = open('yingping.csv','a+',encoding='utf-8')
    csv_writer = csv.writer(f)
    for data in data:
        csv_writer.writerow(data)
    f.close()
def geturl(baseurl):
    l = []
    for i in range(0, 671):
        l.append(i*20)
    for i in range(0, 671):
        l[i] = "https://movie.douban.com/subject/26794435/reviews?start=" + str(l[i])
    for i in range(0,671):
        print(l[i])
    return l


def savefiletodown(url):
    l=geturl(url)
    for i in range(0,671):
        data=getdata(l[i])
        print("正在爬取"+l[i]+"的影评")
        savefile(data)
url = "https://movie.douban.com/subject/26794435/reviews"
savefiletodown(url)