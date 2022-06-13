# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:03:09 2022
@FileName: 2467.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2467

투 포인터

"""


N = int( input() );

a,b = 0, 1

lst  = [ int( i ) for i in input().split() ]
answer = [ lst[ 0 ] , lst[ N - 1 ] ]
lt, rt = 0, N - 1 ;

mini = lst[ lt ] + lst[ rt ];

while lt < rt:
    mini = ( lst[ lt ] + lst [ rt ] )
    if( abs( p_sum ) < sum0 ):
        answer[ a ], answer[ b ] = lst[ lt ], lst[ rt ];
        sum0 = abs( p_sum )
     
    if( p_sum < 0 ):
        lt += 1
    
    elif( p_sum > 0 ):
        rt -= 1
    else:
        break;

        
print( answer[ a ], answer[ b ] )