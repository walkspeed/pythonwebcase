# -*- coding:utf-8 -*-

import web
import sys
import os

class stalkerDB:
    def loadCfg(self,types):
        for itype in types:
            self.loadmac( itype )
            self.loadid( itype )

    def loadmac( self, itype ):
            filename = './macCfg/'+itype+'/macfile'
            macfile = open( filename )
            
            if macfile == None:
                return
            
            setattr(self,itype+'_macarr',[])
            macarr = getattr(self,itype+'_macarr')
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
            print 'loadmac macarr : ', macarr
            macfile.close()

    def loadid( self, itype ):
            filename = './macCfg/'+itype+'/idfile'
            mapfile = open( filename )
            
            if mapfile == None:
                return
            
            setattr(self,itype+'_mapdict',{})
            mapdict = getattr(self,itype+'_mapdict')
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

    def hasMac( self, itype, mac ):
        macarr = getattr(self,itype+'_macarr')

        if macarr == None:
            return False

        if mac in macarr:
            return True

        return False
        

    def findId( self, itype, mac ):
        mapdict = getattr(self,itype+'_mapdict')

        if mapdict == None:
            return ''

        if mac in mapdict.keys():
            return mapdict[mac]
        
        return ''

    def saveId( self, itype, mac, id ):
        macarr = getattr(self,itype+'_macarr')
        mapdict = getattr(self,itype+'_mapdict')

        if macarr == None:
            return False
        
        if mapdict == None:
            return False

        mapdict[mac] = id

        filename = './macCfg/'+itype+'/idfile'
        authfile = open(filename,'a' )
        authfile.write( mac+';'+id+'\n' )
        authfile.close()
        return True

stalker_db = stalkerDB()
stalker_db.loadCfg(['stalker'])

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

        if len(param[0]) < 24:
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
        
    def updataMac(self):
        self.loadMacData()
        self.validMacarr()
        raise web.seeother('/index',True)

    def updataDev(self):
        self.loadDeviceData()
        self.validMacarr()
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
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            if len(line) < 2:
                continue
            self.macarr.append(line)
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
            line = line.replace('\r','')
            devicInfo = line.split(';')
            if len(devicInfo) < 2:
                continue

            self.mapdict[devicInfo[0]] = devicInfo[1]

        mapfile.close()

    def validMacarr( self ):
        for allotitem in self.mapdict.values():
            if allotitem in self.macarr:
                self.macarr.remove( allotitem )

class macConfig:
    def loadCfg(self,types):
        for itype in types:
            self.loadmac( itype )
            self.loadid( itype )
            self.validmac( itype )

    def loadmac( self, itype ):
            filename = './macCfg/'+itype+'/macfile'
            macfile = open( filename )
            
            if macfile == None:
                return
            
            setattr(self,itype+'_macarr',[])
            macarr = getattr(self,itype+'_macarr')
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

    def loadid( self, itype ):
            filename = './macCfg/'+itype+'/idfile'
            mapfile = open( filename )
            
            if mapfile == None:
                return
            
            setattr(self,itype+'_mapdict',{})
            mapdict = getattr(self,itype+'_mapdict')
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

    def validmac( self, itype ):
            mapdict = getattr(self,itype+'_mapdict')
            macarr = getattr(self,itype+'_macarr')
            for allotitem in mapdict.values():
                if allotitem in macarr:
                    macarr.remove( allotitem )

    def findmac( self, itype, id ):
        mapdict = getattr(self,itype+'_mapdict')

        if mapdict == None:
            return ''

        if id in mapdict.keys():
            return mapdict[id]
        
        return ''

    def getnewid( self, itype, id ):
        macarr = getattr(self,itype+'_macarr')
        mapdict = getattr(self,itype+'_mapdict')

        if macarr == None:
            return ''
        
        if mapdict == None:
            return ''
        
        retstr = macarr[0]
        macarr = macarr[1:]

        mapdict[id] = retstr

        filename = './macCfg/'+itype+'/idfile'
        authfile = open(filename,'a' )
        authfile.write( id+';'+retstr+'\n' )
        authfile.close()
        return retstr

clirequest = cmd()
macConfigs = macConfig()
macConfigs.loadCfg(['u51'])

class request:
    def GET(self,argv):
        print __file__.split('\\')[-1],' request argv ',argv
        cmdparse = argv.split(':')
        if len(cmdparse) == 2:
            return clirequest.response(cmdparse[1])

class reponseCmd:
    def response(self,request):
        requestitems = request.split(';')
        print '[reponseCmd.response] requestitems : ', requestitems
        if hasattr( self, requestitems[0] ):
            operator = getattr(self,requestitems[0])
            if len(requestitems) < 2:
                return operator()
            else:
                return operator(requestitems[1:])
        return None

    def authorize(self,param):
        global macConfigs
        retstr = macConfigs.findmac( self.deviceType, param[0] )
        if retstr == '':
            retstr = macConfigs.getnewid( self.deviceType, param[0] )
        return retstr


    def authorize2(self,param):
        global stalker_db
        print 'authorize2 param : ', param
        if len(param) < 2:
            print 'authorize2 len(param) < 2'
            return ''

        hasmac = stalker_db.hasMac( self.deviceType, param[0].upper() )
        if hasmac == False:
            print 'authorize2 hasmac == False'
            return ''
			
        retstr = stalker_db.findId( self.deviceType, param[0].upper() )
        if retstr == '':
            retstr = param[1]
            stalker_db.saveId(self.deviceType, param[0].upper(), retstr)
        print 'authorize2 retstr : ', retstr
        return retstr

class U51Cmd(reponseCmd):
    def __init__(self):
        self.deviceType = 'u51'

    def GET(self,argv):
        print __file__.split('\\')[-1],' U51Cmd argv ',argv
        cmdparse = argv.split(':')
        if len(cmdparse) == 2:
           return self.response(cmdparse[1])

class stalkerRequest(reponseCmd):
    def __init__(self):
        self.deviceType = 'stalker'

    def GET(self, argv):
        print __file__.split('\\')[-1],' stalker cmd argv ',argv
        cmdparse = argv.split(':')
        print 'stalkerRequest len(cmdparse) : ', len(cmdparse)
        if len(cmdparse) == 2:
           return self.response(cmdparse[1])
        
        if len(cmdparse) > 2:
            param = None
            for item in cmdparse[1:]:
                if param == None:
                    param = item
                else:
                    param += ':'+item

            return self.response(param)

        return None			

requrls = ('/stalker/(.*)','stalkerRequest','/u51/(.*)','U51Cmd','/(.*)','request')

reqk_app = web.application(requrls, locals())

def addUrls( app ):
    app.add_mapping( '/request', reqk_app )
