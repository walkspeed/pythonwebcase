#-*- coding:utf-8 -*-
import requests

try:
    response = requests.get('http://localhost:8080/request/cmd:authorize;1QZ7PUNTXJIL6VA9K58DMYS6')#('http://117.78.33.205:18080/request/cmd:authorize;1QZ7PUNTXJIL6VA9K58DMYS2')
except:
    print "response raise error"
else:
    print 'status code:',response.status_code
    print response.text
