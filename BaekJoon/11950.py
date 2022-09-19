# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:14:15 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

white, blue, red = 0,1,2;
x, y = map( int, input().split() );

val = [ [ 0, 0, 0 ] for _ in range( x ) ]

Mn = x * y + 1

sumgraph = [ [ 0, 0, 0 ] for _ in range( x ) ]

for i in range( x ):
    row = input();
    w,r,b = 0,0,0;
    
    for ch in row:
        if( ch == 'W'):
            w +=1
        elif( ch == 'R' ):
            r += 1
        else:
            b += 1
    
    val[ i ] = [ y - w, y - b, y - r ]

sumgraph[ 0 ] = val[ 0 ][ : ]

for i in range( 1, x ):
    for j in range( 3 ):
        sumgraph[ i ][ j ] = sumgraph[ i - 1 ][ j ] + val[ i ][ j ]


perm = [];

lst = [ i for i in range( 1, x - 1 ) ]

for w in lst:
    for b in lst:
        if( ( w + b ) >= x ):
            continue;
        
        perm.append( ( w, b, x - ( w + b ) ) )
    
    
for case in perm:
    w, b, r = case;
    sum_ =  sumgraph[ w - 1 ][ white ] + ( sumgraph[ ( w + b ) - 1 ][  blue  ] - sumgraph[ w - 1 ][ blue ] )  + ( sumgraph[ ( w + b + r ) - 1 ][ red ] - sumgraph[ ( w + b ) - 1 ][ red ] )
    
                                                                                                                 
    Mn = min( Mn, sum_ )
    
print( Mn )
