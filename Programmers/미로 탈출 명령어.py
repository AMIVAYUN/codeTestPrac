# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:54:45 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


answer = "";
import sys;

sys.setrecursionlimit( 10**6 )
'''

아무리 bfs기반의 loop가 관리가 쉽고 이해하기 용이하다 해도 최단거리 문제에선 dfs를 먼저 고려하자 
# bfs는 매번 거리연산으로 통과 but 속도는 10ms가량 차이남.
'''
def dfs( dxy, n, m, x, y, r, c, k, word,now, cnt ):
    global answer;
    if answer != 'z' * k:
        return
    diff = abs( now[ 0 ] - r ) + abs( now[ 1 ] - c )
    if( diff + cnt > k ):
        return
    
    if( cnt == k and ( r, c ) == now ):
        answer = word;
        return;
    
    
    # 깊이 우선으로 가보자
    
    
    for i in range( 4 ):
        dx, dy, w = dxy[ i ];
        nx = now[ 0 ] + dx;
        ny = now[ 1 ] + dy;
    
        if( 0 <= nx < n and 0<= ny < m ):
            if( cnt + 1 <= k ):
                dfs( dxy, n, m, x, y, r, c, k, word + w, (nx, ny ), cnt + 1 )
# Heap을 사용해 k번째가 나오면 바로 리턴해보자
#SOL2 TIMEOUT
def bfs( n, m, x, y, r, c, k ):
    
    '''
    추가 검산 미리 못가는지 파악
    해당 연산 추가를 통해 태케4 통과 but 여전히 time out
    
    '''
    
    diff = abs( r - x ) + abs( c - y ); # abs 추가하여 7 8 번 추가 통과
    
    if( ( diff % 2) != (k % 2) or diff > k ):
        return "z" * k;
    
    import heapq
    answer = 'z' * k;
    x -= 1; y -= 1;
    r -= 1; c -= 1;
  
    con = ( x, y );
    cnt = 0;
    heap = [];
    
    heapq.heapify( heap );
    
    dxy = [ ( 1, 0, "d" ), ( -1, 0, "u" ), ( 0 , -1, "l" ), ( 0, 1, "r" ) ];
    
    
    heapq.heappush( heap,( "", 0, con ) ) 
    while heap:
        if( heap[ 0 ][ 0 ] > answer ):
            break;
            
        word, cnt, pos = heapq.heappop( heap );
        if( abs( pos[ 0 ] - r ) + abs( pos[ 1 ] - c ) + cnt > k ):
            continue;
            
        if( answer != 'z' * k ):
            break;
        
        if( cnt == k ):
            if( pos == ( r, c ) ):
                return word;
            continue;    
            
        for i in range( 4 ):
            dx, dy, w = dxy[ i ];
            nx = pos[ 0 ] + dx;
            ny = pos[ 1 ] + dy;
            
            if( 0<= nx < n and 0<= ny < m ):
                if( word + w <= answer and cnt + 1 <= k):
                    heapq.heappush( heap,( word + w , cnt + 1 , ( nx, ny ) ) ) 

        
    return answer;
def solution(n, m, x, y, r, c, k):
    global answer;
    # n by m graph
    # x y to r c
    # distance = k
    # 중복 도착 가능
    ''''''
    #answer = bfs( n, m, x, y, r, c, k );
    diff = abs( r - x ) + abs( c - y );
    
    if( ( diff % 2 != k % 2 ) or ( diff > k ) ):
 
        return "impossible"
    '''
    dxy = [ ( 1, 0, "d" ), ( -1, 0, "u" ), ( 0 , -1, "l" ), ( 0, 1, "r" ) ];
    
    dxy = list( sorted( dxy, key = lambda x: x[ 2 ] ) );
    
    answer = 'z' * k;
    x -= 1; y -= 1;
    r -= 1; c -= 1;
    '''
    #dfs( dxy, n, m, x, y, r, c, k, "", (x,y) , 0 )
    
    answer = bfs( n, m, x, y, r, c, k )
    
    
    
    return answer if answer != 'z' * k else "impossible"

'''
#SOL1 TIMEOUT
def bfs( n, m, x, y, r, c, k ):
    answer = 'z' * k;
    x -= 1; y -= 1;
    r -= 1; c -= 1;
    from collections import deque;
    con = ( x, y );
    cnt = 0;
    dq = deque(  );
    
    dxy = [ ( 1, 0, "d" ), ( -1, 0, "u" ), ( 0 , -1, "l" ), ( 0, 1, "r" ) ];
    
    
    dq.append( ( con, 0, "") ) 
    while dq:
        pos, cnt, word = dq.popleft();
        
        if( word > answer ):
            continue;
        
        if( cnt == k ):
            if( pos == ( r, c ) ):
                answer = min( answer, word );
                
            continue;
        
        
        for i in range( 4 ):
            dx, dy, w = dxy[ i ];
            nx = pos[ 0 ] + dx;
            ny = pos[ 1 ] + dy;
            
            if( 0<= nx < n and 0<= ny < m ):
                if( word + w <= answer and cnt + 1 <= k):
                    dq.append( ( ( nx, ny ), cnt + 1, word + w ) )
        
    return answer ;
def solution(n, m, x, y, r, c, k):
    # n by m graph
    # x y to r c
    # distance = k
    # 중복 도착 가능
    answer = bfs( n, m, x, y, r, c, k )
    
    
    
    
    
    return answer if answer != 'z' * k else "impossible"
    
'''
    
    dxy = [ ( 1, 0, "d" ), ( -1, 0, "u" ), ( 0 , -1, "l" ), ( 0, 1, "r" ) ];
    
    
    heapq.heappush( heap,( "", 0, con ) ) 
    while heap:
        if( heap[ 0 ][ 0 ] > answer ):
            break;
            
        word, cnt, pos = heapq.heappop( heap );
        
        if( word > answer ):
            continue;
        
        if( cnt == k ):
            if( pos == ( r, c ) ):
                return word;
            continue;    
            
        for i in range( 4 ):
            dx, dy, w = dxy[ i ];
            nx = pos[ 0 ] + dx;
            ny = pos[ 1 ] + dy;
            
            if( 0<= nx < n and 0<= ny < m ):
                if( word + w <= answer and cnt + 1 <= k):
                    heapq.heappush( heap,( word + w , cnt + 1 , ( nx, ny ) ) ) 

        
    return answer;
def solution(n, m, x, y, r, c, k):
    global answer;
    # n by m graph
    # x y to r c
    # distance = k
    # 중복 도착 가능
    ''''''
    #answer = bfs( n, m, x, y, r, c, k );
    diff = abs( r - x ) + abs( c - y );
    
    if( ( diff % 2 != k % 2 ) or ( diff > k ) ):
 
        return "impossible"
    
    
    
    answer = 'z' * k;
    x -= 1; y -= 1;
    r -= 1; c -= 1;

    dfs( n, m, x, y, r, c, k, "", (x,y) , 0 )
    
    
    
    
    
    return answer if answer != 'z' * k else "impossible"

solution( 	3, 4, 2, 3, 3, 1, 5 )
