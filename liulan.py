from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome('D:/chromedriver.exe',options=options)
url="https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html"
driver.get(url)
html=driver.page_source
bf1 = BeautifulSoup(html, 'lxml')
result=bf1.find_all(class_='sf-edu-wenku-id-div_class_1 div_class_1 rtcscontent')
for each_result in result:
	bf2 = BeautifulSoup(str(each_result), 'lxml')
	texts = bf2.find_all('p')
	for each_text in texts:
		main_body = BeautifulSoup(str(each_text), 'lxml')
		for each in main_body.find_all(True):
			if each.name == 'span':
				print(each.string.replace('\xa0',''),end='')
			elif each.name == 'br':
				print('')






