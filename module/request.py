# -*- coding:utf-8 -*-

import web
import sys
import os

requrls = ('/(.*)','request')

class cmd:
    def __init__( self ):
        self.loadMacData()
        self.loadDeviceData()

        self.validMacarr()

    def response(self,request):
        requestitems = request.split(';')
        if hasattr( self, requestitems[0] ):
            operator = getattr(self,requestitems[0])
            if len(requestitems) < 2:
                return operator()
            else:
                return operator(requestitems[1:])
        return None

    def authorize(self,param):
        if len(self.macarr) == 0:
            return ''

        if param[0] in self.mapdict.keys():
            return self.mapdict[param[0]]

        retstr = self.macarr[0]
        self.macarr = self.macarr[1:]

        self.mapdict[param[0]] = retstr
        authfile = open( self.idfile,'a' )
        authfile.write( param[0]+';'+retstr+'\n' )
        return retstr
    def updata(self):
        self.loadMacData()
        self.validMacarr()
        print '[cmd.updata] macarr[0] : ',self.macarr[0]
        raise web.seeother('/index',True)

    def loadMacData( self ):
        self.inifile = 'macfile'

        macfile = open( self.inifile )

        self.macarr = []
        while 1:
            line = macfile.readline()
            if not line:
                break
            if len(line) < 2:
                continue
            self.macarr.append(line.replace("\n", ""))
        macfile.close()

    def loadDeviceData( self ):
        self.idfile = 'idfile'

        mapfile = open( self.idfile )
        self.mapdict = {}

        while 1:
            line = mapfile.readline()
            if not line:
                break

            line = line.replace('\n','')
            devicInfo = line.split(';')
            if len(devicInfo) < 2:
                return

            self.mapdict[devicInfo[0]] = devicInfo[1]

        mapfile.close()

    def validMacarr( self ):
        for allotitem in self.mapdict.values():
            if allotitem in self.macarr:
                self.macarr.remove( allotitem )

clirequest = cmd()

class request:
    def GET(self,argv):
        print __file__.split('\\')[-1],' argv ',argv
        cmdparse = argv.split(':')
        if len(cmdparse) == 2:
            return clirequest.response(cmdparse[1])

reqk_app = web.application(requrls, locals())

def addUrls( app ):
    app.add_mapping( '/request', reqk_app )
