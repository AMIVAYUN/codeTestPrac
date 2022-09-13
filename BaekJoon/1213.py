# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 10:15:40 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


str0 = input();

from collections import defaultdict;


ddit = defaultdict( int );


for ch in str0:
    ddit[ ch ] += 1;
    
leng = len( str0 );
ans = [ "" for _ in range( leng ) ] ;


srkeys = sorted( ddit.keys() );

idx = 0;


for key in srkeys:
    
    while( ddit[ key ] > 1 ):
             
        ans[ idx ], ans[ -1 * ( idx + 1 ) ] = key,key;
            
        idx += 1;
            
        ddit[ key ] -= 2;


if( idx != leng // 2 and list( ddit.values() ).count( 1 ) > 1 ):
    print( "I'm Sorry Hansoo" );
    
else:
    if( leng % 2 ):
        lst = list( ddit.items() );
        
        for tg in lst:
            if( tg[ 1 ] == 1 ):
                ans[ idx ] = tg[ 0 ];
                break;
                
        
        
    print( ''.join( ans ) ) 

