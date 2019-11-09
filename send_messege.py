from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import win32api
import win32con


def send_messege(phonenumber1):
	#58同城
	driver = webdriver.Chrome('D:/chromedriver.exe')
	driver.get("https://passport.58.com/login/?path=https%3A//nj.58.com/%3Futm_source%3Dmarket%26spm%3Du-2d2yxv86y3v43nkddh1.BDPCPZ_BT%26pts%3D1573300221264&PGTID=0d100000-000a-cebf-2481-f9a035b294f5&ClickID=2")
	driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/img").click()
	driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[1]/span[2]").click()
	input01=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/input")
	input01.send_keys(phonenumber1)
	driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/span").click()
	sleep(2)
	#51job
	driver.get("https://login.51job.com/login.php?isjump=0&loginway=1&lang=c&url=")
	input01=driver.find_element_by_id("loginname")
	input01.send_keys(phonenumber1)
	driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/form/div[4]/span").click()
	sleep(2)
#今日招聘
	driver.get("https://www.jrzp.com/login_0.shtml")
	driver.find_element_by_id("verifyLogin").click()
	input01=driver.find_element_by_id("phone1")
	input01.send_keys(phonenumber1)
	driver.find_element_by_id("hqyzm-sendverifycode").click()
	sleep(2)
#中聘网
	driver.get("https://www.cnzp.cn/login/")
	driver.find_element_by_id("mobile_login").click()
	input01=driver.find_element_by_id("usermoblie")
	input01.send_keys(phonenumber1)
	driver.find_element_by_id("send_msg_tip").click()
	sleep(2)

# def send_zhilianzhaopin(phonenumber1):
# 	driver = webdriver.Chrome('D:/chromedriver.exe')
# 	driver.get("https://login.51job.com/login.php?isjump=0&loginway=1&lang=c&url=")
# 	input01=driver.find_element_by_id("loginname")
# 	input01.send_keys(phonenumber1)
# 	driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/form/div[4]/span").click()

# def send_zhilianzhaopin(phonenumber1):
# 	driver = webdriver.Chrome('D:/chromedriver.exe')
# 	driver.get("http://www.stzp.cn/jw/register1.aspx")
# 	input01=driver.find_element_by_id("ctl00_ContentPlaceHolder1_ContactMobile")
# 	input01.send_keys(phonenumber1)
# 	driver.find_element_by_id("yzm").click()


# def send_zhilianzhaopin(phonenumber1):
# 	driver = webdriver.Chrome('D:/chromedriver.exe')
# 	driver.get("https://bj.wendu.com/zt/chk/?comefrom=baidu_Jingpin_C_G_0527_02515_0053612&renqun_youhua=256915")
# 	input01=driver.find_element_by_name("phone")
# 	input01.send_keys(phonenumber1)
# 	driver.find_element_by_id("LXB_CONTAINER").click()


send_messege(17550231993)