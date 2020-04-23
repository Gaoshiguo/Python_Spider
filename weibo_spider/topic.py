import requests
import json
import re
import os
import time,random
os.chdir('C:/Users/dell/Desktop')
import pandas as pd
from w3lib.html import remove_tags
base_url='''
https://m.weibo.cn/api/container/getIndex?containerid=1008082daf12cb79491a80017ae2546cc6f49f_-_feed&luicode=10000011
&lfid=100103type%3D533%26t%3D10%26q%3D%E4%B8%9C%E9%87%8E%E5%9C%AD%E5%90%BE&since_id=4487749686029266
'''
head_list=["Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
   ]
ip=['114.101.42.16:65309',
    '220.179.255.7:8118',
    '103.44.145.182:8080',
    '115.223.7.110:80']
proxy={'http':random.choice(ip)}
header={'user-agent':random.choice(head_list)}
pat='since_id=(.*)'
inf=[]
for page in range(1,300):
    try:
        r=requests.get(base_url,headers=header,proxies=proxy)
        df=json.loads(r.text)
        since_id=df.get('data').get('pageInfo').get('since_id')
        data=df.get('data').get('cards')[0].get('card_group')
        for item in data:
            send_time=item.get('mblog').get('created_at')
            content=remove_tags(item.get('mblog').get('text'))
            inf.append([send_time,content])
        base_url=re.sub(pat,'since_id='+str(since_id),base_url)
        print('第{}页写入完毕'.format(page))
        time.sleep(random.randint(3,5))
    except:
        print('未爬到数据')
inf1=pd.DataFrame(inf,columns=['发布时间','内容'])
inf1.to_csv('daily_comment.csv',index=False,encoding='gb18030')
