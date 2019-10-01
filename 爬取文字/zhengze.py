from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
driver = webdriver.Chrome('D:/chromedriver.exe')
driver.get("https://wenku.baidu.com/view/5b1ef2cfbf23482fb4daa58da0116c175e0e1e0a.html")
page=driver.find_element_by_xpath("//*[@id='html-reader-go-more']/div[2]/div[1]/p")
driver.execute_script('arguments[0].scrollIntoView();', page) #拖动到可见的元素去
driver.find_element_by_xpath("//*[@id='html-reader-go-more']/div[2]/div[1]/p").click()
html=driver.page_source
bf1 = BeautifulSoup(html, 'lxml')
result=bf1.find_all(class_='page-count')
num=BeautifulSoup(str(result),'lxml').span.string
count=eval(repr(num).replace('/', ''))
page_count=int(count)
for i in range(1,page_count+1):
	result=bf1.find_all(id="pageNo-%d"%(i))
	for each_result in result:
		bf2 = BeautifulSoup(str(each_result), 'lxml')
		texts = bf2.find_all('p')
		for each_text in texts:
			main_body = BeautifulSoup(str(each_text), 'lxml')
			s=main_body.get_text()
			print(s)
			f=open("baiduwenku.txt","a",encoding="utf-8")
			f.write(s)
			f.flush()
			f.close()