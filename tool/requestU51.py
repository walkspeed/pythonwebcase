#-*- coding:utf-8 -*-
import requests
"""
try:
    response = requests.get('http://localhost:8080/request/cmd:authorize;33D65AF3FB7E97A8DBF6D425')#('http://117.78.33.205:18080/request/cmd:authorize;1QZ7PUNTXJIL6VA9K58DMYS2')
except:
    print "response raise error"
else:
    print 'status code:',response.status_code
    print response.text

try:
    response = requests.get('http://localhost:8080/request/cmd:authorize;u51;33D65AF3FB7E97A8DBF6D443')#('http://117.78.33.205:18080/request/cmd:authorize;u51;1QZ7PUNTXJIL6VA9K58DMYS2')
except:
    print "response u51 raise error"
else:
    print 'status u51 code:',response.status_code
    print response.text
"""
try:
    #response = requests.get('http://117.78.33.205:18080/request/u51/cmd:authorize;1QZ7PUNTXJIL6VA9K58DMY31')#('http://localhost:8080/request/u51/cmd:authorize;33D65AF3FB7E97A8DBF6D443')
    response = requests.get('http://117.78.33.205:18080/request/u51/cmd:authorize;33D6A1D3538F22D216F68927')#('http://localhost:8080/request/u51/cmd:authorize;33D65AF3FB7E97A8DBF6D443')
except:
    print "response u51 raise error"
else:
    print 'status u51 code:',response.status_code
    print response.text
