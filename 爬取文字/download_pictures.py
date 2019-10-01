# -*- coding:UTF-8 -*-
import requests
if __name__ == '__main__':
	target = 'http://unsplash.com/napi/feeds/home'
	req = requests.get(url=target,verify=False)
	print(req.text)

