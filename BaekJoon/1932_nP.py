# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:14:59 2022
@FileName: 1932.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/submit/1932/44836672
"""
#ans

def main():
    N = int( input() );
    lst = [];
    if( N == 1 ):
        print( int( input( ) ) );
        return;
    for _ in range( N ):
        lst.append( list(map( int, input().split() ) ) );
    

    dp = [ [ 0 ] * len( lst[ i ] ) for i in range( len( lst ) ) ]
    
    dp[ 0 ][ 0 ] = lst[ 0 ][ 0 ];

    
    
    for i in range( N ):
        for j in range( len( lst[ i ] ) ):
            if( j == 0 ):
                dp[ i ][ j ] = dp[ i - 1 ][ j ] + lst[ i ][ j ]
                
            elif( j == i ):
                dp[ i ][ -1 ] = dp[ i - 1 ][ -1 ] + lst[ i ][ -1 ];
            else:
                dp[ i ][ j ] = max( dp[ i - 1 ][ j - 1 ], dp[ i - 1 ][ j ] ) + lst[ i ][ j ];
            
    
    print( max( dp[ N - 1 ] ) );




if( __name__ == "__main__"):
    main()
    


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


        
        
    
    