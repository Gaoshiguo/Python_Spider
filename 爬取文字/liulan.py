from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
driver = webdriver.Chrome('D:/chromedriver.exe')
driver.get("https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html")
page = driver.find_element_by_xpath("//*[@id='html-reader-go-more']/div[1]")
driver.execute_script('arguments[0].scrollIntoView();', page) #拖动到可见的元素去
time.sleep(3)
driver.find_element_by_xpath("//*[@id='html-reader-go-more']/div[2]/div[1]/p").click()
html=driver.page_source
bf1 = BeautifulSoup(html, 'lxml')
result=bf1.find_all(id="pageNo-2")
for each_result in result:
		bf2 = BeautifulSoup(str(each_result), 'lxml')
		texts = bf2.find_all('p')
		for each_text in texts:
			main_body = BeautifulSoup(str(each_text), 'lxml')
			print(main_body.get_text())






