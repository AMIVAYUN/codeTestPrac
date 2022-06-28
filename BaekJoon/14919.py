# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 19:17:47 2022
@FileName: 14919.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/14919
"""


def reff2():
    m = int( input() );
    
    
    lst = list( map( float, input().split() ) ); 
     
    print( "m: ", m , " list: ", lst );
    
    rs = [ 0 ] * m;
    
    lst = [ int( i * ( 10 ** 6 ) ) for i in lst ]
    
    for i in range( 0, m ):
        k = 10 ** 6 / m;
        if( k.is_integer() ):
            k0, k1 = k * i , k * ( i + 1 );
            
        else:
            k0, k1 = ( k * i ) + 1, k * ( i + 1 ) + 1;
        
        for j in range( len( lst ) ):
            if( k0 <= lst[ j ] < k1 ):
                rs[ i ] += 1;
            
    
    for i in rs:
        print( i , end = " ");
#reff2();


def reff3():
    
    m = int( input() );
    
    
    lst = [ i[ 2: ].ljust( 6,"0") for i in input().split() ] ;
    rs = [ 0 ] * m;
    lst = [ int( i ) for i in lst ];
    for i in range( 0, m ):
        k = 10 ** 6 / m;
        if( k.is_integer() ):
            k0, k1 = k * i , k * ( i + 1 );
            
        else:
            k = int( k + 0.1 ) 
            k0, k1 = ( k * i ) + 1, k * ( i + 1 ) + 1;
        
        for j in range( len( lst ) ):
            if( k0 <= lst[ j ] < k1 ):
                rs[ i ] += 1;
            
    
    for i in rs:
        print( i , end = " ");
    
reff3()