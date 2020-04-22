import requests
import json
import re

headers = {#请求标题头
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Mobile Safari/537.36',
'cookie':'ALF=1589868041; _T_WM=26865146473; SUHB=0WGcn_wkaWsgRF; SCF=AqoPz2A9EDn-BNkoDHfO9QsTFfkEosOGPUOzdgZjYwAdrjCe6oOYpI7bLC4kJ-qM43I6LF-rJ6jWRob5T1Dgn7o.; SUB=_2A25zn5txDeRhGeNL7FMX-CzIyz-IHXVRYyU5rDV6PUJbktANLWLxkW1NSPlfi3TIC2hIw9Bqff4k2MUthzLhCBGY; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFDXp7pMyxQ8snrrnTI-xVd5JpX5KzhUgL.Fo-fS02c1hzXehe2dJLoIEWKUPWLMbH8SCHFeF-RxbH8SCHFeF-RxbH81CHWBb-415tt; XSRF-TOKEN=dad71d; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174'#请填写自己的cookie
}

page = 1
def get_post(url):
    response = requests.get(url)
    data = response.json()
    blog = data["data"]["cards"]
    for card in blog:
        mblog = card.get("mblog")
        if mblog:
            user = mblog['user']['screen_name']
            post_number = mblog['reposts_count']
            comment_number = mblog['comments_count']
            content=mblog['text']
            text = re.sub(r'<a.*$','',content)
            print("用户:'%s'" % (user) + "发表的有关哪吒的微博:'%s'"%(text)+"的转发数为：%s" % (post_number) + "评论数为：%s" % (comment_number))

for i in range(0,10):
    url = r"https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E5%93%AA%E5%90%92&page_type=searchall&page=" + str(
        page)
    get_post(url)
    page = page + 1




# response = requests.get(url)
# data = response.json()
# blog = data["data"]["cards"]
# for card in blog:
#     mblog = card.get("mblog")
#     if mblog:
#         user = mblog['user']['screen_name']
#         post_number = mblog['reposts_count']
#         comment_number = mblog['comments_count']
#         print("用户%s"%(user)+"发表的有关杨超越的微博的转发数为：%s"%(post_number)+"评论数为：%s"%(comment_number))