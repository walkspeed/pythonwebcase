# -*- coding:utf-8 -*-

def getMac( number ):
    return '00:00:00:00:%02x:%02x' % ( ( number >> 8 ) & 255, number & 255 )
def makemac( count ):
    mf = open('macfile','w+')
    for i in range( count ):
        mac = getMac( i )
        mf.write( mac + '\n' )

    mf.close()

def makeMacFromRange():
    range1begin = ['00','11','AD','83','96','B0']
    range1end = ['00','11','AD','83','9A','AC']

    range2begin = ['00','11','AD','83','9A','B0']
    range2end = ['00','11','AD','83','9C','BD']

    mf = open('macfile','w+')

    a1 = int( 'b0',16 )
    a2 = int( '96',16 )
    for i in range(0,1021):
        if a1 > 255:
            a1 = 0
            a2 = a2 + 1

        strmac = '00:11:ad:83:%02x:%02x\n' % ( a2, a1 )
        mf.write(strmac)
        a1 = a1 + 1

    a1 = int( 'b0',16 )
    a2 = int( '9a',16 )
    for i in range(0,526):
        if a1 > 255:
            a1 = 0
            a2 = a2 + 1

        strmac = '00:11:ad:83:%02x:%02x\n' % ( a2, a1 )
        mf.write(strmac)
        a1 = a1 + 1

    mf.close()

if __name__ == '__main__':
    makeMacFromRange()
