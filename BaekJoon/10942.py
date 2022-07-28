# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:33:11 2022
@FileName: 10942.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/10942
"""

def f1():
    def isPalindrome( length ,lst ):
        if( length % 2 ):
            rs = lst[ : length // 2 ] + lst[ length //2 : ]
            comp = [ 0 ] * length;
            for i in range( length // 2 ):
                comp[ i ], comp[ -i -1 ] = rs[ i ], rs[ i ]; 
                
            comp[ length // 2 ] = rs[ length //2 ];
            return comp == rs
        else:
            rs = lst[ : length // 2 ]  + lst[ length //2 : ];
            comp = [ 0 ] * length;
            for i in range( length // 2 ):
                comp[ i ], comp[ -i -1 ] = rs[ i ], rs[ i ]; 
            return comp == rs

    N = int( input() );

    lst = list( map( int, input().split() ) );

    M = int( input() );


    for i in range( M ):
        a, b = map( int, input().split() );
        a -= 1;
        print( int( isPalindrome( b - a, lst[ a: b ] ) ) );


# 0 0, 0 1, 0 2, 0 3, 0 4, 0 5, 0 6, x

# 0 0, 1 1, 2 2, 3 3, 4 4, 5 5, 6 6 -> 0 1, 1 2,     


def f2():
    n = int( input() );

    lst = list( map( int, input().split() ) );

    m = int( input() );
    
    dp = [ [ 0 ] * n for _ in range( n + 1 ) ];
    
    
    for bias in range( n ):
        for x in range( n - bias ):
            y = x + bias;
            
            if( x == y ):
                dp[ x ][ y ] = 1;
            
            elif( x == y - 1 ):
                dp[ x ][ y ] = int( lst[ x ] == lst[ y ] );
            
            else:
                dp[ x ][ y ] = int( dp[ x + 1 ][ y - 1 ] == 1 and lst[ x ] == lst[ y ] );
                
                
    for i in range( m ):
        a, b = map( int, input().split() );
        
        print( dp[ a - 1 ][ b - 1 ] );
        
    
def main():
    f2()
    

if( __name__ == "__main__" ):
    main();

