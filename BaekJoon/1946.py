# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 23:38:48 2023
@FileName: 1946.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1946
"""
'''
초기 소스 생각해보니 pop( 0 ) == O ( N ) 이다.

T = int( input() );

for i in range( T ):
    
    ans = 1;
    k = int( input() );
    lst = [];
    for j in range( k ):
        ab = list( map( int, input().split() ) )
        lst.append( ab );

    lst = list( sorted( lst, key = lambda x:( x[ 0  ]) ) );
    
    Mn = lst.pop( 0 )[ 1 ];

    
    while lst:
        val = lst.pop( 0 )[ 1 ];
        
        if( Mn > val ):
            Mn = val;
            ans += 1;
        

    
    print( ans );
'''   
    
import sys;

T = int( sys.stdin.readline() );

for i in range( T ):
    
    ans = 1;
    k = int( sys.stdin.readline() );
    lst = [];
    for j in range( k ):
        ab = list( map( int, sys.stdin.readline().split() ) )
        lst.append( ab );

    lst = list( sorted( lst, key = lambda x:( -x[ 0  ]) ) );
    
    Mn = lst.pop()[ 1 ];

    
    while lst:
        val = lst.pop()[ 1 ];
        
        if( Mn > val ):
            Mn = val;
            ans += 1;
        

    
    print( ans );
            
        

    
    