#-*- coding:utf-8 -*-
import requests
import json

token = None
random = None
def getcss():
	try:
		url = 'http://mag.pandaiptv.net/stalker_portal/external/settings/style/okno_720.css'
		headers = {'Accept': 'text/css,*/*;q=0.1','Referer': 'http://mag.pandaiptv.net/stalker_portal/external/settings/g_local.html', \
				   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) qtweb1 Safari/538.1', \
				   'Cookie': 'mac=00%3A1A%3A79%3A95%3A98%3A18; PHPSESSID=1b722htpbg4jtu3aasvf14qea3', \
				   'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,*', 'Host': 'mag.pandaiptv.net'}
		response = requests.get(url, headers=headers)
	except:
		print "response raise error"
	else:
		print 'status code:',response.status_code
		print response.text

getcss()
