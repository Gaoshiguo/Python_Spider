from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:/chromedriver.exe')
driver.get("https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html")
page = driver.find_element_by_xpath("//*[@id='html-reader-go-more']/div[2]/div[1]/span/span[2]")
driver.execute_script('arguments[0].scrollIntoView();', page) #拖动到可见的元素去
driver.find_element_by_xpath("//*[@id='html-reader-go-more']/div[2]/div[1]/p").click()
