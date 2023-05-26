# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:55:51 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


from collections import deque, defaultdict

Mx = '0';

visit = defaultdict( lambda : defaultdict( int ) );

num, k = input().split();


k = int( k );


dq = deque();

visit[ 0 ][ num ] = 1; 

dq.append( ( list( num ), 0 ) );

leng = len( num );

while dq:
    
    now, cnt = dq.popleft();
    
    if( cnt == k ):
        Mx = max( Mx, ''.join( now ) );
        continue;        
    for i in range( leng - 1 ):
        for j in range( i + 1, leng ):
            if( i == 0 and now[ j ] == '0' ):
                continue
            
            now[ i ], now[ j ] = now[ j ], now[ i ];
            
            if( cnt + 1 <= k and visit[ cnt + 1 ][ ''.join( now ) ] == 0 ):
                visit[ cnt + 1 ][ ''.join( now ) ] = 1;
                dq.append( ( now[:], cnt + 1 ) );
    
            now[ i ], now[ j ] = now[ j ], now[ i ];



print( Mx if Mx != '0' else -1 );