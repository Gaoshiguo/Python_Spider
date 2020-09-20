import requests
from lxml import etree
import re
import json
import csv
import time
import random

# 获取网页源代码
def get_page(url):
    headers = {
        'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    cookies = {
        'cookie':'bid="dDi4Ej8VlXw"; ll="118159"; __utmc=30149280; __utmz=30149280.1600437860.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D598C964736D559B4D7D0F397D5D3970A|7b30a828dfd8ac5099cc76928e5bf247; __gads=ID=d08666ef0c486f08:T=1600437871:S=ALNI_Mb1ckWHCXnWqUaGt4WluOeyT7YFRw; __yadk_uid=EWypb2CJs37Tg6KZqoPFEQvzQhJa1Kfz; push_doumail_num=0; push_noty_num=0; __utmv=30149280.22363; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1600488752%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin_popup%3Flogin_source%3Danony%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.71960709.1600437860.1600478971.1600488755.3; __utmt=1; _pk_id.100001.8cb4=f83ff8e7058502e7.1600439393.3.1600488959.1600479789.; __utmb=30149280.7.9.1600488959515; dbcl2="223635887:Q7KbPvWO3oU"'
    }
    response = requests.get(url=url,headers=headers,cookies=cookies)
    html = response.text
    return html

# 解析网页源代码，获取下一页链接
# def parse4link(html,base_url):
#     link = None
#     html_elem = etree.HTML(html)
#     url = html_elem.xpath('//div[@id="paginator"]/a[@class="next"]/@href')
#     if url:
#         link = base_url + url[0]
#     return link
def parse4link(html,base_url):
    link = None
    html_elem = etree.HTML(html)
    url = html_elem.xpath('//div[@id="paginator"]/a[@class="next"]/@href')
    if url:
        link = base_url + url[0]
    return link



# 解析网页源代码，获取数据
def parse4data(html):
    html = etree.HTML(html)
    agrees = html.xpath('//div[@class="comment-item"]/div[2]/h3/span[1]/span/text()')
    authods = html.xpath('//div[@class="comment-item"]/div[2]/h3/span[2]/a/text()')
    stars = html.xpath('//div[@class="comment-item"]/div[2]/h3/span[2]/span[2]/@title')
    contents = html.xpath('//div[@class="comment-item"]/div[2]/p/span/text()')
    data = zip(agrees,authods,stars,contents)
    return data

# 打开文件
def openfile(fm):
    fd = None
    if fm == 'txt':
        fd = open('douban_comment.txt','w',encoding='utf-8')
    elif fm == 'json':
        fd = open('douban_comment.json','w',encoding='utf-8')
    elif fm == 'csv':
        fd = open('douban_comment.csv','w',encoding='utf-8',newline='')
    return fd

# 将数据保存到文件
def save2file(fm,fd,data):
    if fm == 'txt':
        for item in data:
            fd.write('----------------------------------------\n')
            fd.write('agree：' + str(item[0]) + '\n')
            fd.write('authod：' + str(item[1]) + '\n')
            fd.write('star：' + str(item[2]) + '\n')
            fd.write('content：' + str(item[3]) + '\n')
    if fm == 'json':
        temp = ('agree','authod','star','content')
        for item in data:
            json.dump(dict(zip(temp,item)),fd,ensure_ascii=False)
    if fm == 'csv':
        writer = csv.writer(fd)
        for item in data:
            writer.writerow(item)

# 开始爬取网页
def crawl():
    moveID = input('请输入电影ID：')
    while not re.match(r'\d{8}',moveID):
        moveID = input('输入错误，请重新输入电影ID：')
    base_url = 'https://movie.douban.com/subject/' + moveID + '/comments'
    fm = input('请输入文件保存格式（txt、json、csv）：')
    while fm!='txt' and fm!='json' and fm!='csv':
        fm = input('输入错误，请重新输入文件保存格式（txt、json、csv）：')
    fd = openfile(fm)
    print('开始爬取')
    link = base_url
    while link:
        print('正在爬取 ' + str(link) + ' ......')
        html = get_page(link)
        link = parse4link(html,base_url)
        data = parse4data(html)
        save2file(fm,fd,data)
        time.sleep(random.random())
    fd.close()
    print('结束爬取')

if __name__ == '__main__':
    crawl()