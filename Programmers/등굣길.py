# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:30:56 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""



def solution(m, n, puddles):
    
    '''
     0, 0 to m - 1, n -1 
     
     각 좌표는 자기 자리 기준 위나 왼쪽만 보면 된다.
    '''
    answer = 0
    
    dp_graph = [ [ 0 ] * m for _ in range( n ) ] 
    dp_graph [ 0 ][ 0 ] = 1;
    for x in range( n ):
        for y in range( m ):
            if( [ y + 1 , x + 1 ] not in puddles ):
                tmp1 = dp_graph[ x - 1 ][ y ] if( x - 1 >= 0 ) else 0;
                tmp2 = dp_graph[ x ][ y - 1 ] if( y - 1 >= 0 ) else 0;
                dp_graph[ x ][ y ] += ( tmp1 + tmp2 );
                dp_graph[ x ][ y ] %= 1000000007;
            
    return dp_graph[ n - 1 ][ m - 1 ];