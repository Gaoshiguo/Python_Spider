import requests
import json
import re

headers = {#请求标题头
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Mobile Safari/537.36',
'cookie':'ALF=1589868041; _T_WM=26865146473; SUHB=0WGcn_wkaWsgRF; SCF=AqoPz2A9EDn-BNkoDHfO9QsTFfkEosOGPUOzdgZjYwAdrjCe6oOYpI7bLC4kJ-qM43I6LF-rJ6jWRob5T1Dgn7o.; SUB=_2A25zn5txDeRhGeNL7FMX-CzIyz-IHXVRYyU5rDV6PUJbktANLWLxkW1NSPlfi3TIC2hIw9Bqff4k2MUthzLhCBGY; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFDXp7pMyxQ8snrrnTI-xVd5JpX5KzhUgL.Fo-fS02c1hzXehe2dJLoIEWKUPWLMbH8SCHFeF-RxbH8SCHFeF-RxbH81CHWBb-415tt; XSRF-TOKEN=dad71d; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174'#请填写自己的cookie
}
max_id = False
page_end = 10#爬取页数，自己修改
page_start = 1
u = 1
while page_start<page_end:#当start小于end时进行循环
    if max_id == False:#因为微博第一页和其他页的参数不一样所以需要区分开来
        url = "https://m.weibo.cn/comments/hotflow?id=4496202160709117&mid=4496202160709117&max_id_type=0"#第一页不包含max_id
        json = requests.get(url)#访问评论json数据
    else:
        url = "https://m.weibo.cn/comments/hotflow?id=4496202160709117&mid=4496202160709117&max_id="+str(max_id)+"&max_id_type=0"
        json = requests.get(url,headers = headers)#访问评论json数据
    json = json.json()#转化数据
    max_id = json['data']['max_id']#第二页的max_id在第一页中 第三页在第二页中...以此类推
    jsons = json['data']['data']
    page_start = page_start+1#自增
    for j in jsons:
        text = j['text']
        user = j['id']
        text = re.sub(r'<(.+?)>','',text)#删除表情包
        print("第"+str(u)+"个用户id为%s"%(user)+str(u)+"评论内容:%s"%(text))
        u = u+1
print('完成')
