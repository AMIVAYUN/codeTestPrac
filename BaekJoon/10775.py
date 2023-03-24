# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:48:55 2023
@FileName: 10775.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/10775
"""

'''
오늘은 신승원의 생일이다.

박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를
 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다.
 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다.
 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?



'''
N = int( input() );
P = int( input() );

parent = [ i for i in range( N + 1 ) ];

answer = 0;
from collections import deque;
ps = deque( );

def union( x, y ):
    root_x, root_y = find( x ), find( y );
    if( x > y ):
        parent[ root_x ] = root_y;
    else:
        parent[ root_y ]= root_x;
        
        
def find( x ):
    if( parent[ x ] != x ):
        parent[ x ] = find( parent[ x ] );
        
    
    return parent[ x ];


for i in range( P ):
    ps.append( int( input() ) );
    

while ps:

    now = ps.popleft();
    
    p = find( now );

    if( p == 0 ):
        break;
    
    union( p, p - 1 );
    answer += 1;

print( answer )
        
    
'''
Time out
N = int( input() );
P = int( input() );
gate = [ 0 ] * ( N + 1 );
answer = 0;
def batch( p ):
    for i in range( p, -1, -1 ):
        #비었으면.
        if( gate[ i ] == 0 ):
            return i;
    
    return i;




for i in range( P ):

    p = int( input() );
    if( gate[ p ] == 0 ):
        gate[ p ] = p;
        answer += 1;
    else:
        parent = batch( p );
        if( parent == 0 ):
            break;
        
        gate = gate[ :parent ] + gate[ parent + 1: p + 1 ] + [ p ] + gate[ p + 1 : ];
    
        answer += 1;


print( 'answer: ', answer );

'''