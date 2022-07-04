# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 19:25:55 2022

@author: 주석
"""

N , K = map( int, input().split() );

lst = list( map( int, input().split() ) )
'''
lst = [ ( lst[ i ], i ) for i in range( N )]

lst = sorted( lst )

lt = 0 ; rt = N;
ans = 0;
while lt<= rt:
    mid = ( lt + rt ) // 2
    
    if( lst[ mid ] > K ):
        rt = mid - 1;
    
    else:
        ans = mid;
        lt = mid + 1;
    

print( ans )
'''
rs = []
for i in range( N ):
    if( lst[ i ] < K ):
        rs.append( lst[ i ] )
        
for i in rs:
    print( i, end = " " )