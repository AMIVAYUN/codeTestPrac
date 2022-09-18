# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:59:06 2022
@FileName: 2529.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2529
"""
#Memory Out
def t1():



    N = int( input() );

    Mn =( ''.join( ['9']*( N + 1 ) ) )
    Mx = '0';

    lst = [ i for i in range( 10 ) ];

    comp = list( input().split() )

    import itertools

    perm = list( itertools.permutations( lst, N + 1 ) )



    for case in perm:
        flag = True;
        for idx in range( N ):
            if( not( getComparison( case[ idx ], case[ idx + 1 ], comp[ idx ] ) ) ):
                flag = False;
                break;
            
        
        if( flag ):
            Mn = min( Mn, ''.join( [ str( i ) for i in case ] ))
            Mx = max( Mx, ''.join( [ str( i ) for i in case ] ) )

    print( Mn )
    print( Mx )
    
    
def getComparison( a, b, str0 ):
    if( str0 == "<" ):
        return a < b;
    else:
        return a > b;

def MinBackTracking( depth, str0 ):
    global Mn,Mx;
    if( depth == N ):
        Mn = min( str0, Mn );
        Mx = max( str0, Mx );
        return
    
    for i in range( 10 ):
        
        if( getComparison( str0[ depth ], str( i ) , comp[ depth ] ) and str( i ) not in str0 ):

            MinBackTracking(depth + 1 , str0 + str( i ) )
            

N = int( input() );    
Mn = "9" * ( N + 1 )
Mx = "0"

comp = list( input().split() );

for i in range( 10 ):
    res = [];
    MinBackTracking( 0, str( i ) );


print( Mx )
print( Mn )