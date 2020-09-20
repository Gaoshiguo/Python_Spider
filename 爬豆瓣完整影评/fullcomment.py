from lxml import etree
import csv
import requests
def get_page(url):
    headers = {
        'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    cookies = {
        'cookie':'bid="dDi4Ej8VlXw"; ll="118159"; __utmc=30149280; _vwo_uuid_v2=D598C964736D559B4D7D0F397D5D3970A|7b30a828dfd8ac5099cc76928e5bf247; __gads=ID=d08666ef0c486f08:T=1600437871:S=ALNI_Mb1ckWHCXnWqUaGt4WluOeyT7YFRw; __yadk_uid=EWypb2CJs37Tg6KZqoPFEQvzQhJa1Kfz; push_doumail_num=0; push_noty_num=0; __utmv=30149280.22363; ap_v=0,6.0; __utma=30149280.71960709.1600437860.1600516118.1600522715.9; __utmb=30149280.0.10.1600522715; __utmz=30149280.1600522715.9.5.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1600522725%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin_popup%3Flogin_source%3Danony%22%5D; _pk_id.100001.8cb4=f83ff8e7058502e7.1600439393.9.1600522725.1600516169.; _pk_ses.100001.8cb4=*; dbcl2="223635887:Qj+ZfmdXORk"; ck=nfwI'
    }
    response = requests.get(url=url,headers=headers,cookies=cookies)
    html = response.text
    return html

def getlinks(url):
    html = get_page(url)
    Html = etree.HTML(html)
    links = Html.xpath('//div[@class="main-bd"]/h2/a/@href')
    return links
def get_detail(url):
    html = get_page(url)
    Html = etree.HTML(html)
    comments=Html.xpath('//div[@class="review-content clearfix"]')
    times=Html.xpath('//span[@class="main-meta"]/text()')
    names=Html.xpath('//header[@class="main-hd"]/a/span/text()')
    useful=Html.xpath('//div[@class="main-panel-useful"]/button[1]')
    useless=Html.xpath('//div[@class="main-panel-useful"]/button[2]')
    shoucang=Html.xpath('//span[@class="react-num"]/text()')
    zhuanfa=Html.xpath('//span[@class="rec-num"]/text()')
    stars = Html.xpath('//header[@class="main-hd"]/span[1]/@title')
    if useful==[]:
        use=[]
    else:
        use=useful[0].xpath('string(.)').strip()
    if comments==[]:
        comment=[]
    else:
        comment=comments[0].xpath('string(.)').strip()
    if useless==[]:
        unuse=[]
    else:
        unuse=useless[0].xpath('string(.)').strip()
    if shoucang==[]:
        scnum=[]
    else:
        scnum=shoucang
    if zhuanfa==[]:
        renum=zhuanfa
    else:
        renum=zhuanfa[0]
    if names==[]:
        name=[]
    else:
        name=names[0]
    if times==[]:
        time=[]
    else:
        time=times[0]
    if stars==[]:
        star=[]
    else:
        star=stars[0]
    f = open('download.csv','a+',encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow([name,time,star,comment,use,unuse,scnum,renum])
    f.close()

def geturl(starturl):
    l = []
    for i in range(0, 671):
        l.append(i*20)
    for i in range(0, 671):
        l[i] = "https://movie.douban.com/subject/26794435/reviews?start=" + str(l[i])
    for i in range(0,671):
        print(l[i])
    return l
def tem(url):
    l=geturl(url)
    for i in range(0,len(l)):
        baseurl=l[i]
        links=getlinks(baseurl)
        for i in range(0,len(links)):
            lin=links[i]
            get_detail(lin)
url="https://movie.douban.com/subject/26794435/reviews"
tem(url)

