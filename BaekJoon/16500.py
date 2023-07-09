# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 21:37:18 2023

@author: 주석
"""

from collections import defaultdict;

ddit = defaultdict( lambda: 1 );

flag = False;
def dfs( idx, c ):
    global lst, s, flag, ddit;

    if( flag ):
        return;
    
    if( idx == len( s ) ):
        if( c == s ):
            flag = True;
        return
    origin = c[:]
    for next in lst:
        if( len( next ) + idx <= len( s ) and s[ idx: idx + len( next ) ] == next ):
            c += s[ idx: idx + len( next ) ]
            if( ddit[ c ] ):
                ddit[ c ] = 0;
                
                dfs( idx + len( next ), c );
            c = origin;


s = input();

n = int( input() );

lst = [];

for i in range( n ):
    lst.append( input() );


for c in lst:
    if( s[ : len( c ) ] == c ):
        dfs( len( c ), c );

print( 1 if flag else 0 );
    