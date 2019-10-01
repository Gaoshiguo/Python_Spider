import requests
from bs4 import BeautifulSoup
server='http://www.biqukan.com/'
url="http://www.biqukan.com/1_1094/"
req=requests.get(url)
req.encoding=req.apparent_encoding
data=req.text
bf=BeautifulSoup(data,"html.parser")
con=bf.find_all('div',class_='listmain')
hr=BeautifulSoup(str(con[0]))
a=hr.find_all('a')
for each in a:
	print(each.string, server + each.get('href'))
