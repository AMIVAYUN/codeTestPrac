# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 12:15:56 2022
@FileName: 2295.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2295
"""


# 뒤에서 부터 O( N**3 )
def f1():
    sett = set();

    N = int( input() );


    for i in range( N ):
        sett.add( int( input() ) );
    lst = list( sett );
    from collections import defaultdict;
    ans = 0;
    start = 1; 
    cond = False;
    for i in reversed( lst ):
        tg = i;
        
        for j in range( N - start ):
            tg2 = tg - lst[ j ];
            ddit = defaultdict( int );
            
            for k in range( N - start ):
                if( lst[ k ] == lst[ j ] ):
                    continue;
                
                if( ddit[ tg2 ] == lst[ k ] ):
                    cond = True
                    ans = tg
                    break;
                else:
                    ddit[ tg2 ] = tg2 - lst[ k ]
            if( cond ):
                break;
        if( cond ):
            break;
        
        start = 1; 

    print( ans );

def getItem( num ):
    return 1 << ( num );
def f2():
    
    from collections import defaultdict;
    import bisect;
    ddit = defaultdict( list );
    sett = set();

    N = int( input() );

    cond = False;    
    start = 1;
    for i in range( N ):
        sett.add( int( input() ) );
    
    sett2 = set()
    
    for x1 in sett:
        for x2 in sett:
            
            sett2.add( x1 + x2 );
        
            
    
    rs = 0;
    
    for target in sett:
        for x3 in sett:
            if( target - x3 in sett2):
                rs = max( rs, target );
    
    print( rs )
            
    
            




f2();
