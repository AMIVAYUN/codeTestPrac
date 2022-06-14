# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:39:51 2022
@FileName: 2493.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/status?user_id=amiva&problem_id=2493&from_mine=1
"""


#2493

N = int( input() );

lst = list( map( int, input().split() ) )



answer = [ 0 ] * N ;

stack = [  ];

if( N == 1 ):
    print( answer[ 0 ] )

for i in range( len( lst ) -1 , -1, -1 ):
    while stack and lst[ stack[ -1 ] ] < lst[ i ]:
        val= stack.pop();
        answer[ val ] = i + 1;
    
    stack.append( i )
        
    
    
for i in answer:
    print( i, end = " ")
    