# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:46:51 2023
@FileName: 9184.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/9184
"""


'''

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    

'''
dp = [ [ [ 0 ] * 21 for _ in range( 21 ) ] for k in range( 21 ) ];

def w( a, b, c ):
    
    
    if( a <= 0 or b <= 0 or c<= 0 ):
        return 1;
    
    if( a > 20 or b > 20 or c > 20 ):
        return w( 20, 20, 20 );
    
    if( dp[ a ][ b ][ c ] ):
        return dp[ a ][ b ][ c ];
    
    
    
    elif a < b and b < c:
        dp[ a ][ b ][ c ] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c);
    
    else:
        
        dp[ a ][ b ][ c ] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1);



    return dp[ a ][ b ][ c ];


while True:
    a, b, c = map( int, input().split() );
    
    if( a == b == c== -1 ):
        break;
    
    
    rs = w( a, b, c );
    str0 = list( 'w(0, 0, 0) = 1' );
    print( 'w('+ str( a ) + ', ' + str( b ) + ', ' + str( c ) + ') = ' + str( rs ) );