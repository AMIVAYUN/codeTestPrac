# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:03:27 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
# 68% Time Out
'''
def find( num ):
    global checker;
    pos = num;
    
    while( checker[ pos ] != pos ):
        pos = checker[ pos ];
    
    return pos;
'''   
'''
이 부분 매우 중요

'''
# 68% TimeOut
def find( num ):
    global checker;
    if( num != checker[ num ] ):
        #num = find( checker[ num ] );
        checker[ num ] = find( checker[ num ] );
    #return num
    return checker[ num ];

def union( a, b ):
    global checker;
    pa, pb = find( a ), find( b );
    if( pa > pb ):
        checker[ pa ] = pb;
    else:
        checker[ pb ] = pa;
        


def check( a, b ):
    if( find( a ) == find( b ) ):
        print( "YES" );
    else:
        print("NO")
        
dit = { 0: union, 1: check }    


n, m = map( int, input().split() );


checker = [ i for i in range( n + 1 ) ];



for i in range( m ):
    oper, a, b = map( int, input().split() );
    
    dit[ oper ]( a, b );
    