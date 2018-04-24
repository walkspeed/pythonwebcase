#-*- coding:utf-8 -*-
import requests
import json

token = None
random = None
def handshake():
	try:
		url = 'http://78.47.168.207/stalker_portal/server/load.php?type=stb&action=handshake&token=&JsHttpRequest=1-xml'
		headers = {'X-User-Agent': 'Model: MAG250','Referer': 'http://mag.pandaiptv.net/stalker_portal/c/', \
				   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) qtweb1 Safari/538.1', \
				   'Accept': '*/*', 'Cookie': 'mac=00%3A1A%3A79%3A95%3A98%3A18; stb_lang=en; timezone=Asia%2FShanghai', \
				   'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,*', 'Host': 'mag.pandaiptv.net'}
		response = requests.get(url, headers=headers)
	except:
		print "response raise error"
	else:
		print 'status code:',response.status_code
		print response.text
        jsdata = json.loads(response.text)
        print 'print jsdata *****************'
        print jsdata['js']
        token = jsdata['js']['token']
        print token
        random = jsdata['js']['random']
        print random
        print jsdata['text']

handshake()

def getprofile():
    try:
		url = 'http://78.47.168.207/stalker_portal/server/load.php?type=stb&action=get_profile&hd=1&ver=ImageDescription:%200.2.18-r19-250;%20ImageDate:%2026%20Fer%202018%2018:36:12%20GMT+0800;;%20PORTAL%20version:%205.0.0;%20API%20Version:%20JS%20API%20version:%20328;%20STB%20API%20version:%20134;%20Player%20Engine%20version:%200x566&num_banks=1&sn=012012N01212&stb_type=MAG250&client_type=STB&image_version=218&video_out=hdmi&device_id=410D4843071DC11648DE2C89485A52851D95892A67F01500C53A8D882EE989A9&device_id2=14DF1165EF610640C2B6A890551BA36C6ADCCB59D745241EB397DDF90D574B3C&signature=9F4E445B238F693F384641F37756ACF00D8CA6F941D3D7088D3BBBF46378E93B&auth_second_step=0&hw_version=1.11-BD-00&not_valid_token=0&metrics=%7B%22mac%22%3A%2200%3A1A%3A79%3A95%3A98%3A18%22%2C%22sn%22%3A%22012012N01212%22%2C%22type%22%3A%22stb%22%2C%22model%22%3A%22MAG250%22%2C%22uid%22%3A%2214DF1165EF610640C2B6A890551BA36C6ADCCB59D745241EB397DDF90D574B3C%22%7D&hw_version_2=&JsHttpRequest=1-xml'
		headers = {'Authorization': 'Bearer %s'%token, 'X-User-Agent': 'Model: MAG250','Referer': 'http://mag.pandaiptv.net/stalker_portal/c/', \
				   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) qtweb1 Safari/538.1', \
				   'Accept': '*/*', 'Cookie': 'mac=00%3A1A%3A79%3A95%3A98%3A18; stb_lang=en; timezone=Asia%2FShanghai; PHPSESSID=r5idk7mj244j9fie38156tkuk2', \
				   'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,*', 'Host': 'mag.pandaiptv.net'}
		response = requests.get(url, headers=headers)
    except:
        print "response raise error"
    else:
        print response.text

getprofile()
