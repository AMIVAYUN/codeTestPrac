# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:09:57 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""



def dis2( x, d ):
    import math;
    return ( (d**2 - x**2) ** 0.5 );

def solution(k, d):
    
    import bisect;
    answer = 0;
    for x in range( 0, d + 1, k ):
        if( x > d ):
            continue;
        answer += 1; #( 0 포함 );
        answer += dis2( x, d ) // k;

    return answer;
'''
# SOL3 37.5 WA
def dis( pos ):
    return ( pos[ 0 ] ** 2 + pos[ 1 ] ** 2 ) ** 0.5;


def dis2( x, d ):
    import math;
    return ( (d**2 - x**2) ** 0.5 );
    
    
def solution(k, d):
    import bisect;
    answer = 0;
    for x in range( d, -1, ( k * -1) ):
        sub = dis2( x, d );
        if( sub > d ):
            continue;
        answer += sub//k + 1;

    return answer;
'''

'''
# SOL2 == 50.0 TIMEOUT * 8 ( 16 );
def dis( pos ):
    return ( pos[ 0 ] ** 2 + pos[ 1 ] ** 2 ) ** 0.5
def solution(k, d):
    answer = 0;
    for x in range( 0, d + 1, k ):
        for y in range( 0, d + 1, k ):
            if( dis( (x , y) ) > d ):
                break;
            
            answer += 1;
            
    return answer;
'''
'''
# SOL 1 == 6.3 TIMEOUT * 15( 16 );
def dis( pos ):
    return ( pos[ 0 ] ** 2 + pos[ 1 ] ** 2 ) ** 0.5
def solution(k, d):
    x = [ k * i for i in range( d + 1 ) ]
    y = x[ : ];
    
    import itertools;
    
    res = list( itertools.product( x, y, repeat = 1 ) );
    
    answer = [ i for i in res if dis( i ) <= d ]

    return len( answer );
    
'''