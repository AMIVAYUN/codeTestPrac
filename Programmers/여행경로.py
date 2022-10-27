# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 00:46:28 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def dfs( route, pos ):
    global visit,ddit,answer, obj;

    if( isNull() ):

        answer.append( route[:] );
        return;
    for i in range( len( ddit[ pos ] ) ):
        tmp = ddit[ pos ][ i ][ : ];
        ddit[ pos ] = ddit[ pos ][ :i ] + ddit[ pos ][ i + 1 : ];
        
        route.append( tmp );
        
        dfs( route, tmp );
        
        route.pop();
        
        ddit[ pos ] = ddit[ pos ][ :i ] + [tmp] + ddit[ pos ][ i : ];
    return

visit = {};
ddit = {};
answer = [];
obj = 0;
def isNull( ):
    global ddit;
    
    for key in ddit:
        if( len( ddit[ key ] ) ):
            return False;
    
    return True;
def solution(tickets):
    
    from collections import defaultdict;
    global visit, ddit,answer, obj;
    answer = [];
    
    ddit = defaultdict( list );
    visit = defaultdict( int );
    for x,y in tickets:
        ddit[ x ].append( y );
        visit[ x ] = 0;
        visit[ y ] = 0;

    obj = len( tickets );
    
    dfs( ["ICN"], "ICN" );
    
    rs = list( sorted( answer, key= lambda x: ''.join( x ) ) );

    return rs[ 0 ];
