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
	print(texts[0].text.replace('\xa0'*8,'\n\n'))
