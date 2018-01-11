# -*- coding:utf-8 -*-
import web
import request

urls = (
    '/','login',
    '/index', 'index',
    '/loadmac','loadmac',
    '/loaddev','loaddev',
    '/request',request.reqk_app,
    '/download/(.*)','download',
    '/upload','upload'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
