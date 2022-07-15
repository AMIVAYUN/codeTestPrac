# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:49:12 2022
@FileName: 1501.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1501
"""

'''
dit = { chr( i ) : 0 for i in range( 65, 91 ) }

dit.update( { chr( i ) : 0 for i in range( 97, 123 ) }  )
'''
def f1():
    ref = {};

    N = int( input() );
    import itertools;
    for i in range( N ):
        str0 = input();
        start, end = str0[ 0 ], str0[ -1 ];
        str0 = str0[ 1:-1 ];
        str0 = str0.replace( " ", "" );
        key = start + end
        
        
        val = "".join( i for i in set( str0 ) );
        
        
        
        if( key in ref ):
            if( val in ref[ key ] ):
                ref[ key ][ val ] += 1;
            
            else:
                ref[ key ][ val ] = 1;
            
        else:
            ref[ key ] = { val: 1 }
        
        
    M = int( input() );

    for i in range( M ):
        str0 = input();
        start, end = str0[ 0 ], str0[ -1 ];
        str0 = str0[ 1:-1 ];
        key = start + end
        val = "".join( i for i in set( str0 ) );
        
        if( key in ref and val in ref[ key ] ):
            print( ref[ key ][ val ] );
        else:
            print( 0 );
def f2():
    ref = {};
    N = int( input() );
    for i in range( N ):
        str0 = input().split();
        for j in str0:
            start, end = j[ 0 ], j[ -1 ];
            sub = j[ 1:-1 ];
            key = j[ 0 ] + j[ -1 ];
            val = "".join( k for k in sub );
            
            if( key in ref ):
                
                ref[ key ][ val ] = 1;
            else:
                ref[ key ] = { val: 1 };

    M = int( input() );
    import itertools;
    
    for i in range( M ):
        sum_ = 1;
        str0 = input().split();
        for j in str0:
            sum_2 = 0;
            start, end = j[ 0 ], j[ -1 ];
            sub = j[ 1:-1 ];
            key = start + end;
            val = "".join( k for k in sub );
            perm = list( itertools.permutations( val, len( val ) ) );
            perm = set( perm );
            
            for k in perm:
                subkey = "".join( k );
                if( key in ref ):
                    if( subkey in ref[ key ] ):
                        sum_2 += 1;
            sum_ *= sum_2;
        
        
        print( sum_ );  
        
     
    

def f3():
    from collections import defaultdict;
    ref = defaultdict( lambda: defaultdict( int ) );
    N = int( input() );
    for i in range( N ):
        str0 = input().split();
        for j in str0:
            sub = j[ 1:-1 ];
            
            if( len( j ) > 1 ):
                key = j[ 0 ] + j[ -1 ];
            else:
                key = j[ 0 ];
            
            if( len( j ) > 2 ):
                subkey = "".join( sorted( sub ) )
            else:
                subkey = ''
            
            
            ref[ key ][ subkey ] += 1;
    M = int( input() );
    
    for j in range( M ):
        ans = 1;
        str0 = input().split();
        
        for j in str0:
            sub = j[ 1: -1 ];
            if( len( j ) > 1 ):
                key = j[ 0 ] + j[ -1 ];
            else:
                key = j[ 0 ];
            
            if( len( j ) > 2 ):
                subkey = "".join( sorted( sub ) )
            else:
                subkey = ''
            ans *= ref[ key ][ subkey ];
        
        print( ans )
f3()          





        
