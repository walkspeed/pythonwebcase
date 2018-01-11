# -*- coding:utf-8 -*-
import web
import session
import request
import code 

urls = (
    '/', code.login,
    '/index', code.index,
    '/loadmac',code.loadmac,
    '/loaddev',code.loaddev,
    '/request',request.reqk_app,
    '/download/(.*)',code.download,
    '/upload',code.upload
)

session.initSession( urls )

if __name__ == "__main__":
    session.getApp().run()
