# -*- coding:utf-8 -*-
import web
import session
import request
import manager 

urls = (
    '/', manager.login,
    '/index', manager.index,
    '/loadmac',manager.loadmac,
    '/loaddev',manager.loaddev,
    '/request',request.reqk_app,
    '/download/(.*)',manager.download,
    '/upload',manager.upload
)

session.initSession( urls )

if __name__ == "__main__":
    session.getApp().run()
