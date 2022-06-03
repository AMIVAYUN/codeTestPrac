# -*- coding: utf-8 -*-
"""
Created on Wed May 25 13:11:18 2022
@FileName: 10026.py
@author: YUNJUSEOK
@Link: https://www.acmicpc.net/problem/10026

DFS

"""
import sys;
sys.setrecursionlimit( int( 1e6 ) )

dx = [ 0, 0, 1, -1 ]
dy = [ 1, -1, 0, 0 ]
N = 0;
lst2 = [];
cnt, cnt2 = 0, 0;

def dfs( lst, x, y ):
    import copy;
    global N,lst2;
    case = copy.deepcopy( lst[ y ][ x ])
    lst[ y ][ x ] = '0'
    if( ord( case ) ^ 0x42 ):
        lst2[ y ][ x ] = 'R';
    else:
        lst2[ y ][ x ] = 'B';
    for i in range( 4 ):
        if( x + dx[ i ] > -1 and x + dx[ i ] < N and y + dy[ i ] > -1 and y + dy[ i ] < N ):
            if( ord( lst [ y + dy[ i ]][ x + dx[ i ] ]) == ord( case ) ):
                
                dfs( lst,x + dx[ i ], y + dy[ i ] )
    

def main():
    import copy;
    lst = [];
    global lst2, N, cnt, cnt2;
  
    N = int( input() );
    
    lst2 = [ [0] * N for _ in range( N ) ]
    
    for i in range( N ):
        lst.append( list(input()) );
    for y in range( N ):
        for x in range( N ):
            if( lst[ y ][ x ] != '0'):
                dfs( lst,x, y );
                cnt += 1;
    
    lst3 = copy.deepcopy( lst2 );
    for y in range( N ):
        for x in range( N ):
            if( lst3[ y ][ x ] != '0'):
                dfs( lst3,x, y );
                cnt2 += 1;
                
if( __name__ == "__main__" ):
    main();

