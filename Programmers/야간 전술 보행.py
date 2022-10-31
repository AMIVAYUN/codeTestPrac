# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:16:44 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


#1 WA
'''
def solution(distance, scope, times):
    answer = 0
    
    work = [ False for _ in range( distance + 1 ) ];
    for i in range( len( times ) ):
    
        table = ( [ True ] * times[ i ][ 0 ] ) + ( [ False ] * times[ i ][ 1 ] );
        mul = ( distance // ( sum( times[ i ] ) ) ) + 1;
        table *= mul;
        
        start, end = scope[ i ];
        
        start -= 1;
        end -= 1;
        
        for idx in range( start, end + 1 ):
            work[ idx ] = table[ idx ];
        
    print( work );
    
    for i in range( distance ):
        if ( work [ i ] ):
            return i + 1;
    return distance;
'''
def solution(distance, scope, times):
    answer = 0 ;
    field = [ False ] * ( distance + 1 ); 
    scope = [ list( sorted( scope[ i ] ) ) for i in range( len( scope ) ) ];
    workers = [ ( scope[ i ], times[ i ] ) for i in range( len( scope ) ) ];
    

    
    workers = sorted( workers )
    
    for worker in workers:
        scope, time = worker;
        
        work , rest = time;
        
        start, end = scope;
    
        schedule = [ True ] * work + [ False ] * rest;
        
        for i in range( start , end + 1 ):
            sub = ( i - 1 ) % sum( time );
            field[ i ] = schedule[ sub ];
    
    for i in range( distance ):
        if( field[ i ] ):
            return i;
    return distance;