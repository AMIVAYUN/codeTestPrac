# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:53:58 2022
@FileName: 1354.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1354
"""

'''
N, P, Q, X, Y = map( int, input().split() );
dit = {}
def getNum( n ):
    print( n );
    global X,Y,P,Q;
    if( n < 1 ):
        return 1;
    
    return getNum( ( n//P ) - X  ) + getNum( ( n//Q ) - Y );

print( getNum( N ) );
'''
'''
memory
def getNum( n ):
    global X,Y,P,Q;
    from collections import deque;
    
    dq = deque();
    sum_ = 0;
    dq.append( n );
    
    while dq:
        pos = dq.popleft();
        if( pos < 1 ):
            sum_ += 1;
            continue;
        
        dq.append( ( pos // P ) - X ); dq.append( ( pos // Q ) - Y );
        
    return sum_

print( getNum( N ) ) 
'''
'''
memory
dp = [ 1 ];
mMx = min( 1 // P - X , 1 // Q - Y );

for i in range( 1, N + 1 ):
    
    a, b = i // P - X if i // P - X > 1 else 0, i // Q - Y if i // Q  - Y > 1 else 0;
    dp.append( dp[ a ] + dp [ b ] );

print( dp[ N ] )

'''
'''
N, P, Q, X, Y = map( int, input().split() );

def getX( N ):
    N_ = N;
    global P,Q,X,Y
    cnt = 0;
    cnt2 = 0;
    while( N > 0 ):
        N = N // P - X
        cnt += 1;
    while N_ > 0:
        N_ = N_ // Q - Y;
        cnt2 += 1;
    return max( cnt, cnt2 );

print( 2**getX( N ) )
'''
N, P, Q, X, Y = map( int, input().split() );
dit = {}
def getNum( n ):
    
    global X,Y,P,Q, dit;
    if( n < 1 ):
        return 1;
    a, b = n // P - X , n // Q - Y;

    if( n in dit ):
        return dit[ n ];
    
    dit[ n ] = getNum( a ) + getNum( b );

    return dit[ n ];

print( getNum( N ) );