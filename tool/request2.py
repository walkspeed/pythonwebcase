#-*- coding:utf-8 -*-
import requests

try:
    s = requests.Session()
    response = requests.get('http://cms235.pandaiptv.net:25461/PkfDkaL7fsLvL_CFPNWT1w/1520328593/001A79959818/34632')
except:
    print "response raise error"
else:
    print 'status code:',response.status_code
    print response.content
