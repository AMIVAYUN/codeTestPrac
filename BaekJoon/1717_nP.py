# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 10:36:00 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def union( a, b ):
    if( a not in ddit ):
        ddit[ a ] = set( [ a ] );
        
    if( b not in ddit ):
        ddit[ b ] = set( [ b ] );
    
    
    ddit[ a ] = ddit[ a ] | ddit[ b ];
    
    ddit[ b ] = ddit[ a ] | ddit[ b ];
    return;

def check( a, b ):
    import sys;
    global ddit;
    if( a not in ddit or b not in ddit ):
        print("NO" );
        return;
        
    if( ddit[ a ] == ddit[ b ] ):
        print( "YES" );
        
    else:
        print( "NO" );
    
    sys.stdin.flush();
    sys.stdout.flush();
    
n, m = map( int, input().split() );

from collections import defaultdict;

logicalDict = { 0: union, 1: check };

ddit = defaultdict( set );


for i in range( m ):
    oper, a, b = map( int, input().split() );
    
 
    logicalDict[ oper ]( a, b );
        

    