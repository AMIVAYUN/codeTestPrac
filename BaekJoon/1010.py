# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:46:46 2022
@FileName: 1010.py ( 다리 놓기 )
@author: YUNJUSEOK
"""

# 조합을 통해 해결하는 문제다 왜냐하면 조합은 순서쌍 1, 3, 4 와 4, 1, 3 을 전부 같은 것으로 보기 때문이다.
def factorial( n ):
    alpha = 1;
    for i in range( 1, n + 1 ):
        alpha *= i ;
    
    return alpha;
def f1( N, M ):
    sum0 = 0;
    if( N == 1 ):
        return M;
    for i in range( 1, N ):
        sum0 += ( N - 1 ) * ( M - i )
        
    return sum0

def f1_1( N, M ):
    sum0 = 0;
    
    return factorial( M ) // ( factorial( N ) * factorial( M - N ) );

def main():
    T = int( input() );
    
    for i in range( T ):
        N,M = input().split();
        result = f1_1( int( N ) , int( M ) );
        print( result );
    
if( __name__ == "__main__" ):
    main()
