# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:22:55 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

from collections import defaultdict;
result = defaultdict( int );
# flag true > 큰거 제거
def dfs( arr, flag, size ):
    global result
    print( arr, flag, size );
    if( size == 1 ):
        result [ arr[ 0 ] ] = 1;
        return;
        
    for idx in range( size ):
        if( idx == size - 1 ):
            if( flag ):
                if( arr[ idx ] > arr[ idx - 1 ] ):
                    
                    dfs( arr[ :idx ], flag, size - 1 );
            else:
                dfs( arr[ :idx ], arr[ idx ] < arr[ idx -  1], size - 1 )
            
        
    
        else:
            if( flag ):
                if( arr[ idx ] > arr[ idx + 1 ] ):
                    
                    dfs( arr[ :idx ] + arr[ idx + 1: ], flag, size - 1 );
            
            else:
                dfs( arr[ :idx ]+ arr[ idx + 1: ], arr[ idx ] < arr[ idx +  1], size - 1 ) 

            
    
def solution(a):
    global result;
    answer = 0 ;
    '''
    임의의 두 풍선 고르고 두 풍선중 하나 터트림
    
    터진 풍선으로 인해 풍선들 사이에 빈 공간이 생기면 빈 공간이 없도록 풍선들을 중앙으로 밀착시킵니다.
    
    여기서 조건이 있다. 인접 두 풍선 중에 번호가 더 작은 풍선을 터트리는 행위는 최대 1번만 가능.
    어떤 시점에서 인접한 두 풍선 중 더 작은 풍선 터트리면 두 풍선을 고르고 번호가 더 큰 풍선만을 터트릴 수 있습니다.
    
    어떤 풍선이 최후까지 남을 수 있나 알아보고 싶다.
    
    
    '''
    
    leng = len( a );


    for idx in range( leng ):
        if( idx == leng - 1 ):
            dfs( a[ :idx ], a[ idx ] < a[ idx -  1], leng - 1 )
            break;
        else:
            dfs( a[ :idx ] + a[ idx + 1: ], a[ idx ] < a[ idx +  1], leng - 1 )
    
    return len( result.keys() );

solution( [ 9, -1, -5 ] )
print( result )