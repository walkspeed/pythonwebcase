# -*- coding:utf-8 -*-
import web
from web import form
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

allowed = (
	('admin','123456'),
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))

render = web.template.render('templates/')

class index:
    def GET(self):
        web.header('Content-Type','text/html;charset=UTF-8')
        return render.index()

class loadmac:
    def GET(self):
        web.header('Content-Type','text/html;charset=UTF-8')
        self.loadMacData()
        return render.loadmac(self.macarr)
    def loadMacData( self ):
        self.inifile = 'macfile'

        macfile = open( self.inifile )

        self.macarr = []
        while 1:
            line = macfile.readline()
            if not line:
                break
            self.macarr.append(line.replace("\n", ""))

        macfile.close()

class loaddev:
    def GET(self):
        web.header('Content-Type','text/html;charset=UTF-8')
        self.loadDeviceData()
        return render.loaddev(self.devarr)
    def loadDeviceData( self ):
        self.idfile = 'idfile'

        mapfile = open( self.idfile )
        self.devarr = []

        while 1:
            line = mapfile.readline()
            if not line:
                break
            self.devarr.append(line.replace("\n", ""))

        mapfile.close()

class login:
	def GET(self):
		return render.login()
	def POST(self):
		i = web.input()
		username = i.get('username')
		passwd = i.get('passwd')
		if (username,passwd) in allowed:
			session.logged_in = True
			web.setcookie('system_mangement', '', 60)
			raise web.seeother('/index')
		else:
			return '<h1>Login Error!!!</h1></br><a href="/login">Login</a>'

BUF_SIZE = 262144

class download:
    def GET(self,filepath):
        f = None
        print '[code.py].[download].[GET].param.filepath : ',filepath
        try:
            filename = 'd:\pythonweb\%s' % filepath
            f = open(filename, "rb")
            web.header('Content-Type','application/octet-stream')
            web.header('Content-disposition', 'attachment; filename=%s' % filepath)
            while True:
                c = f.read(BUF_SIZE)
                if c:
                    yield c
                else:
                    break
        except Exception, e:
            print e
            yield 'Error'
        finally:
            if f:
                f.close()

class upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return render.upload()

    def POST(self):
        x = web.input(myfile={})
        filedir = 'd:\\' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            filename=filename.decode('utf-8')
            fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        raise web.seeother('/upload')

if __name__ == "__main__":
    app.run()
