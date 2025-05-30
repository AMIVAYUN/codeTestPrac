# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:49:40 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


import sys;
sys.setrecursionlimit( int( 1e6 ) );
graph = [set()];
route = [];
visit = [];
answer = 0;
def dfs( n, route, pos, context ):
    global graph, obj, visit,answer;

    if( answer < len( route ) ):
        return
    if( obj == context ):

        answer = min( len( route ), answer );
        return;

    for i in range( 1, n + 1 ):
        if( visit[ i ] == 0 ):
            visit[ i ] = 1;
            prev = context.copy();
            context = context | graph[ i ] | set( [ i ] );
            route.append( i );
            
            dfs( n,route, i, context );
            
            route.pop();
            visit[ i ] = 0;
            context = prev;
            
    
def solution( n, lighthouse ):
    global obj, graph,visit,answer;
    visit = [ 0 ] * ( n + 1 )
    answer = n + 1
    obj = set([ i for i in range( 1, n + 1 ) ] );
    
    graph = [ set() for _ in range( n + 1 ) ];
    
    for x,y in lighthouse:
        graph[ x ].add( y );
        graph[ y ].add( x );
    
    for i in range( 1, n + 1 ):
        visit[ i ] = 1;
        const = set( [ i ] ) | graph[ i ];
        dfs( n,[ i ], i, const );
        visit[ i ] = 0;
    
    return answer;