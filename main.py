# -*- coding:utf-8 -*-
import web
import session
import moduleMgr

"""
urls = (
    '/', manager.login,
    '/index', manager.index,
    '/loadmac',manager.loadmac,
    '/loaddev',manager.loaddev,
    '/request',request.reqk_app,
    '/download/(.*)',manager.download,
    '/upload',manager.upload
)
"""

session.initSession()

"""
mod = my_import("module.request")
mod.addUrls( session.getApp() )

mod = my_import("module.manager")
mod.addUrls( session.getApp() )
"""
if __name__ == "__main__":
    moduleMgr.autoLoadModule(session)
    session.getApp().run()
