# -*- coding:utf-8 -*-

import web
import sys
import os

requrls = ('/(.*)','request')

class cmd:
    def __init__( self ):
        self.types=['u51']
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

    def authorize_notype(self,param):
        if len(self.macarr) == 0:
            return ''

        if len(self.mapdict) > 0:
            if param[0] in self.mapdict.keys():
                return self.mapdict[param[0]]

        retstr = self.macarr[0]
        self.macarr = self.macarr[1:]

        self.mapdict[param[0]] = retstr
        authfile = open( self.idfile,'a' )
        authfile.write( param[0]+';'+retstr+'\n' )
        return retstr

    def authorize_type(self,param):
        macarrname = param[0]+'_macarr'
        print '[authorize_type] macarrname : ',macarrname
        macarr = getattr(self,param[0]+'_macarr')
        if macarr == None:
            print '[authorize_type] macarr == None'
            return ''

        if len(macarr) == 0:
            print '[authorize_type] macarr == 0'
            return ''

        mapdict = getattr(self,param[0]+'_mapdict')
        if len(mapdict) > 0:
            if param[1] in mapdict.keys():
                print ' param[1] in mapdict.keys()'
                return mapdict[param[1]]

        retstr = macarr[0]
        macarr = macarr[1:]

        mapdict[param[1]] = retstr
        authfile = open(param[0]+'_idfile','a' )
        authfile.write( param[1]+';'+retstr+'\n' )
        return retstr

    def authorize(self,param):
        if len(param) > 1:
            return self.authorize_type(param)

        return self.authorize_notype(param)
        
    def updataMac(self):
        self.loadMacData()
        self.validMacarr()
        raise web.seeother('/index',True)

    def updataDev(self):
        self.loadDeviceData()
        self.validMacarr()
        raise web.seeother('/index',True)

    def loadMacData_type(self,types):
        if len(types) < 1:
            return
        
        for devtype in types:
            filename = devtype+'_macfile'
            macfile = open( filename )
            
            if macfile == None:
                return
            
            setattr(self,devtype+'_macarr',[])
            macarr = getattr(self,devtype+'_macarr')
            while 1:
                line = macfile.readline()
                if not line:
                    break
                if len(line) < 2:
                    continue
                line = line.replace("\n", "")
                line = line.replace("\r", "")
                if len(line) < 2:
                    continue
                macarr.append(line)
            macfile.close()

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
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            if len(line) < 2:
                continue
            self.macarr.append(line)
        macfile.close()

        self.loadMacData_type(self.types)

    def loadDeviceData_type(self,types):
        if len(types) < 1:
            return
        
        for devtype in types:
            filename = devtype+'_idfile'
            mapfile = open( filename )
            
            if mapfile == None:
                return
            
            setattr(self,devtype+'_mapdict',{})
            mapdict = getattr(self,devtype+'_mapdict')
            while 1:
                line = mapfile.readline()
                if not line:
                    break

                line = line.replace('\n','')
                line = line.replace('\r','')
                devicInfo = line.split(';')
                if len(devicInfo) < 2:
                    continue

                mapdict[devicInfo[0]] = devicInfo[1]

            mapfile.close()

    def loadDeviceData( self ):
        self.idfile = 'idfile'

        mapfile = open( self.idfile )
        self.mapdict = {}

        while 1:
            line = mapfile.readline()
            if not line:
                break

            line = line.replace('\n','')
            line = line.replace('\r','')
            devicInfo = line.split(';')
            if len(devicInfo) < 2:
                continue

            self.mapdict[devicInfo[0]] = devicInfo[1]

        mapfile.close()
        self.loadDeviceData_type(self.types)

    def validMacarr_type( self, types ):
        if len(types) < 1:
            return

        for devtype in types:
            mapdict = getattr(self,devtype+'_mapdict')
            macarr = getattr(self,devtype+'_macarr')
            for allotitem in mapdict.values():
                if allotitem in macarr:
                    macarr.remove( allotitem )

    def validMacarr( self ):
        for allotitem in self.mapdict.values():
            if allotitem in self.macarr:
                self.macarr.remove( allotitem )
        
        self.validMacarr_type(self.types)

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
