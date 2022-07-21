# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:45:40 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

n, Mx = map( int, input().split() );
lst = [];
for i in range( n ):
    lst.append( int( input() ) );


lst = sorted( lst );
tg = 0;
    
if( len( lst ) == 1 ):
    print( lst[ 0 ] + Mx );
else:
    newlst = [ lst[ i + 1 ] - lst [i ] for i in range( n - 1 )]
    
    while Mx > 0 and tg < len( newlst ):
        diff = newlst[ tg ];
        
        while diff > 0:
            
            for i in range( tg + 1 ):
                if( Mx < 1 ):
                    break;
                
                lst[ i ] += 1
                Mx -= 1
                diff -= 1;
            
        
        tg += 1

    if( Mx > 0 ):
        
        while( Mx > 0 ):
            for i in range( n ):
                if( Mx < 1 ):
                    break;
                lst[ i ] += 1
                Mx -= 1
    
    print( min( lst ) if min( lst ) <  1000000001 else 1000000000 )
    
