from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import win32api
import win32con
VK_CODE ={'enter':0x0D, 'down_arrow':0x28}
#按下键盘
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)

#松开键盘
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

driver = webdriver.Chrome('D:/chromedriver.exe')
driver.get("https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E7%BE%8E%E5%9B%BE%E7%BD%91&step_word=&hs=2&pn=1&spn=0&di=13200&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=113014737%2C3445157660&os=2351244306%2C2367448695&simid=3050896469%2C3730470527&adpicid=0&lpn=0&ln=362&fr=&fmq=1570618921319_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fgss0.baidu.com%2F-vo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2F0df431adcbef7609968039362cdda3cc7dd99e94.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bp7xt_z%26e3Bv54_z%26e3BvgAzdH3Fetjof-8nbml9nnclam-8nbml9nnclamdbdd_z%26e3Bip4s&gsm=&rpstart=0&rpnum=0&islist=&querylist=&force=undefined")
image=driver.find_element_by_xpath('//*[@id="currentImg"]')
action = ActionChains(driver).move_to_element(image)
# ActionChains(driver).context_click(image).perform()
action.context_click(image).perform()
time.sleep(1)
win32api.keybd_event(86, 0, 0, 0)
win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)

keyDown('enter')
keyUp('enter')
time.sleep(1)
print("图片下载完成")