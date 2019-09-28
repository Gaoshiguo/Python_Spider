**以上学习教程均取材于崔庆才大佬的教学**
**第一课我们来学习如何爬取文字，下载一本连载于网页上的小说**
_笔趣看是一个盗版小说网站，这里有很多起点中文网的小说，该网站小说的更新速度稍滞后于起点中文网正版小说的更新速度。并且该网站只支持在线浏览，不支持小说打包下载。因此，本次实战就是从该网站爬取并保存一本名为《一念永恒》的小说，该小说是耳根正在连载中的一部玄幻小说。PS：本实例仅为交流学习，支持耳根大大，请上起点中文网订阅。_
我们先获取这个网站的HTML信息看一下：
```python
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
	target = 'http://www.biqukan.com/1_1094/5403177.html'
	req = requests.get(url = target)
    html = req.text
	bf = BeautifulSoup(html)
	texts = bf.find_all('div', class_ = 'showtxt') 
	print(texts)
```
[!image](https://github.com/Gaoshiguo/Python_Spider/blob/master/image/5.png)
这是第一次跑的结果，好像跟大神的不一样，上面一部分英文说的是什么warning，应该是警告什么的，下面一部分全是乱码，百度了一下，说警告是由于没有为`beautifulsoup`指定解析器，下面的乱码是因为没有设置好编码。
解决办法是：在`bf = BeautifulSoup(html)`这句括号里添加解析器`'html.parser'`
更改后的代码为：
```python
# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
	target = 'http://www.biqukan.com/1_1094/5403177.html'
	req = requests.get(url = target)
	req.encoding=req.apparent_encoding
	html = req.text
	bf = BeautifulSoup(html,'html.parser')
	texts = bf.find_all('div', class_ = 'showtxt') 
	print(texts)
```
[!image](https://github.com/Gaoshiguo/Python_Spider/blob/master/image/6.png)
