# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:32:37 2022
@FileName: 11724.py
@author: YUNJUSEOK
@Link : https://www.acmicpc.net/problem/11724
@Desc : 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
@Input : 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
        (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
        (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
@Output: 첫째 줄에 연결 요소의 개수를 출력.


"""

# => 메모리 초과.
lst = [];
cnt = 0;

def dfs( x, y ):
    global lst;
    lst[ x ][ y ] = 0;
    lst[ y ][ x ] = 0;
    for i in range( len(lst) ):
        if( lst[ y ][ i ] == 1 ):
            dfs( y, i );
    
    return;
            
        
    
    
def main():
    global cnt, lst;
    M, N = map( int, input().split() );

    lst = [ [0] * M for i in range( M ) ];
    
    for i in range( N ):
        a, b = map( int, input().split() );
        lst[ a - 1 ][ b - 1 ] = 1;
        lst[ b - 1 ][ a - 1 ] = 1;
        
    
    for i in range( M ):
        for j in range( M ):
            if( lst[ i ][ j ] == 1 ):
                cnt += 1;
                
                dfs( i, j );


    

    print( cnt );

if( __name__ == "__main__"):
    main();


'''
------------------------------------------------------------------------------------------------------
'''

# 메모리 초과.
import sys;
sys.setrecursionlimit( int( 1e6 ) );
dit = {};
cnt = 0;
visited = {};
def deletein( key ):
    global dit;
    if( visited[ key ] == 0 ):
        return;
    
    visited[ key ] = 0;
        
    for i in dit.get( key ):
        deletein( i );
        
        
        
    
    
    
def main():
    global dit, cnt;
    M, N = map( int, input().split() );
    
    for i in range( 1, M + 1 ):
        dit[ i ] = [];
        visited[ i ] = 1;
    
    for i in range( N ):
        a, b = map( int, input().split() );
        dit[ a ].append( b );
        dit[ b ].append( a );
    
    for i in dit:
        if( visited[ i ] == 1 ):
            cnt += 1;
            deletein( i );
        
    


if(__name__ == "__main__" ):
    main();
    
'''
-----------------------------------------------------------------------------------------------------
'''
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:32:37 2022
@FileName: 11724.py
@author: YUNJUSEOK
@Link : https://www.acmicpc.net/problem/11724
@Desc : 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
@Input : 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
        (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
        (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
@Output: 첫째 줄에 연결 요소의 개수를 출력.


"""

# => 해결.

import sys;
sys.setrecursionlimit( int( 1e5 ) );
lst = [];
cnt = 0;
visited = [];

def dfs( y ):
    global lst,visited;
    visited[ y ] = True
    for i in range( len( lst[y] ) ):
        if( lst[ y ][ i ] == 1 and not( visited[ i ] ) ):
            dfs( i );
    
    return;
            
        
    
    
def main():
    global cnt, lst,visited;
    M, N = map( int, input().split() );

    lst = [ [0] * M for i in range( M ) ];
    visited = [ False ] * M;
    for i in range( N ):
        a, b = map( int, input().split() );
        lst[ a - 1 ][ b - 1 ] = 1;
        lst[ b - 1 ][ a - 1 ] = 1;
    
    
    
    for i in range( M ):
        if( not( visited[ i ] ) ):
            cnt += 1;
            dfs( i );


    

    print( cnt );

if( __name__ == "__main__"):
    main();


