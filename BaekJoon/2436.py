# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 09:59:34 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def GCD( a, b ):
    if( b == 0 ): return a;
    
    else: 
        if( a < b ):
            return GCD( b, a );
        else:
            return GCD( a % b, b );



gcd, lcm = map( int, input().split() );


mul = gcd * lcm;


#( a * b ) // gcd = lcm
a, b = 1, lcm;
stan =  ( ( lcm * gcd ) // gcd , gcd )
Mx = max( gcd, lcm );


for i in range( gcd * 2, Mx + 1 , gcd ):
    
    if( ( lcm * gcd ) % i ):
        continue
    
    
    tg = ( lcm * gcd ) // i + i
    
    if( GCD( tg, i ) != gcd ):
        continue;
    
    if( tg > sum( stan ) ):
        break;
        
    else:
        stan = ( i, tg - i );

for i in sorted( stan ):
    print( i, end = " ")


