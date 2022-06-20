# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:14:59 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def getMaxRoot( val, idx, depth ):
    global lst,res;
    if depth == -1:
        res.append( val );
        return;
    for i in range( idx, -1, -1 ):
        if( len( lst[ depth ] ) > idx > 0 ):
            a, b = idx -1 , idx;
            if( lst[ depth ][ a ] > lst[ depth ][ b ] ):
                getMaxRoot( val + lst[ depth ][ a ], a, depth - 1 );
                
            elif( lst[ depth ][ a ] < lst[ depth ][ b ] ):
                getMaxRoot( val + lst[ depth ][ b ], b, depth - 1 );
            
            else:
                getMaxRoot( val + lst[ depth ][ a ], a, depth - 1 )
                getMaxRoot( val + lst[ depth ][ b ], b, depth - 1 );
        elif( idx == 0 ):
            
            getMaxRoot( val + lst[ depth ][ 0 ], 0, depth - 1 );
        elif( idx == len( lst[ depth ] ) or idx == -1 ):
            
            getMaxRoot( val+ lst[ depth ][ -1 ], -1, depth - 1 );
            
N = int( input() );

lst = [];

for i in range( 1, N + 1 ):
    lst.append( list( map( int, input().split() ) ) )
    
res = [];

a, b = 0, 0;
for i in range( N - 1, -1, -1 ):
    a += lst[ i ][ 0 ]
    b += lst[ i ][ -1 ]
    
res.append( max( a, b ) );

for i in range( 1, N - 1 ):
    getMaxRoot( lst[ N - 1 ][ i ], i ,N - 2 );

print( max( res ) );


        
        
    
    