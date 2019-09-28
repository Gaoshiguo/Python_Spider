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
![image](https://github.com/Gaoshiguo/Python_Spider/blob/master/image/5.png)
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
![image](https://github.com/Gaoshiguo/Python_Spider/blob/master/image/6.png)
可以看到我们熟悉的内容了
然后我们只需要这些文字，其中的一些`<br><\br>`标签和空格并不是我们所需要的。所以我们需要通过beautifuisoup库来进行删选。
使用replace方法，剔除空格，替换为回车进行分段。 在html中是用来表示空格的。replace(’\xa0’*8,’\n\n’)就是去掉下图的八个空格符号，并用回车代替
```python
# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/5403177.html'
     req = requests.get(url = target) html = req.text
     bf = BeautifulSoup(html)
     texts = bf.find_all('div', class_ = 'showtxt')
     print(texts[0].text.replace('\xa0'*8,'\n\n'))
```

![image](https://github.com/Gaoshiguo/Python_Spider/blob/master/image/7.png)
可以看到已经提取出网页中的文字了

现在看我们学会提取某一章的文字了，然后我们需要提取出每一章的链接，然后顺着这每一个链接爬取每一个链接的文字，这样就完成了正本电子书的下载了。
我们进入这本书的目录页，查看目录的网页结构
![image](https://github.com/Gaoshiguo/Python_Spider/blob/master/image/8.png)
还是像之前一样
```python
# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/'
     req = requests.get(url = target)
     html = req.text
     div_bf = BeautifulSoup(html)
     div = div_bf.find_all('div', class_ = 'listmain')
     print(div[0])
```
![image](https://github.com/Gaoshiguo/Python_Spider/blob/master/image/9.png)
我们可以看见每一个章节的链接都位于a标签之中，因此我们需要使用beautifulsoup提取其中所有的a标签
```python
hr=BeautifulSoup(str(con[0]))
a=hr.find_all('a')
for each in a:
	print(each.string, server + each.get('href'))
```
![image](https://github.com/Gaoshiguo/Python_Spider/blob/master/image/10.png)
现在我们每一章的链接有了，每一章的名字也有了，爬取每一章的文本内容的代码也有了，接下来就是整合一下了，然后写入到一个txt文档里，就完成了爬取。
完整代码如下：
[完整代码](https://github.com/Gaoshiguo/Python_Spider/blob/master/download_note.py)
