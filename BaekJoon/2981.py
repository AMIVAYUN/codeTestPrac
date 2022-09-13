# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:19:35 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def gcd( a, b ):
    if( b == 0 ):
        return a;
    else:
        if( a < b ):
            return gcd( b, a );
        else:
            return gcd( a % b, b );

N = int( input() );


lst = [];
for i in range( N ):
    lst.append( int( input() ) )

lst = sorted( lst )

lst = [ lst[ i + 1 ] - lst[ i ] for i in range( N - 1 ) ]

start = lst[ 0 ]
for num in lst[ 1: ]:
    start = gcd( start, num );

ans = [];

for i in range( 2, start + 1 ):
    if( start % i ):
        continue
    
    ans.append( i );


for i in ans:
    print( i, end = " " );