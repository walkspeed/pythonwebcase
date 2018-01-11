import web

app = None
session = None

"""
def initSession( urls ):
    global app
    app = web.application( urls, globals() )
    global session
    session = web.session.Session(app,web.session.DiskStore('sessions'))
"""
def initSession():
    global app
    app = web.application()
    global session
    session = web.session.Session(app,web.session.DiskStore('sessions'))
	
def getApp():
    global app
    return app

def getSession():
    global session
    return session
