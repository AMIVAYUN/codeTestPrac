# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:32:42 2022
@FileName: 17229.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/status?user_id=amiva&problem_id=17299&from_mine=1

By Stack O(2N)
"""

#17299
N = int( input() )
lst = [ int( i ) for i in input().split() ];

dit = {};

for i in range( N ):
    if( lst[ i ] in dit ):
        
        dit[ lst[ i ] ] += 1;
    
    else:
        
        dit[ lst[ i ] ] = 1;

result = [ -1 ] * N;
stack = [ 0 ];

for i in range( 1, N ):
    while stack and dit[ lst[ stack[ -1 ] ] ] < dit[ lst[ i ] ]:
        idx = stack.pop();
        
        result[ idx ] = lst[ i ];
    
    stack.append( i )
        
    
for i in range( N ):
    print( result[ i ], end= " ")

   
