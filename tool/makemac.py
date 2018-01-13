# -*- coding:utf-8 -*-

def getMac( number ):
    return '00:00:00:00:%02x:%02x' % ( ( number >> 8 ) & 255, number & 255 )
def makemac( count ):
    mf = open('macfile','w+')
    for i in range( count ):
        mac = getMac( i )
        mf.write( mac + '\n' )

    mf.close()

if __name__ == '__main__':
    makemac( 5000 )
