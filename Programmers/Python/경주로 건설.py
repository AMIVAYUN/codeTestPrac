# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:19:50 2023
@FileName: 경주로 건설.py
@author: YUNJUSEOK
@Link:https://school.programmers.co.kr/learn/courses/30/lessons/67259#
"""
""

visit = [];
graph = [];
import sys;
sys.setrecursionlimit( int( 1e6 ) );
def dfs(  N, now, cnt, dir0 ):
    global graph; global visit;

    dxy = [ [ 0, 1 ], [ 1, 0 ], [ -1, 0 ], [ 0, -1 ] ];
    
    
    
    x, y = now;
    
    if( x == N - 1 and y == N - 1 ):
        return;
    
    
    
    for idx in range( 4 ):
        nowdir = ( dir0 + idx ) % 4;
        dx, dy = dxy[ nowdir ];
        
        nx = x + dx; ny = y + dy;
        if( nowdir == dir0 ):
            bias = 100;
        else:
            bias = 600;
        
        
        if( 0<= nx < N and 0 <= ny < N ):
            if( graph[ nx ][ ny ] == 0 ):
                
                if( visit[ nx ][ ny ][ nowdir ] > cnt + bias ):
                    visit[ nx ][ ny ][ nowdir ] = cnt + bias; 
                    next = ( nx, ny );
                    nextcnt = cnt + bias;
                    dfs(  N, next, nextcnt , nowdir );
    
    
    
def solution(board):
    global visit, graph;

    graph = board;
    N = len( board[ 0 ] );
    
    visit = [ [ [ float('inf') for i in range( 4 ) ] for j in range( N ) ] for k in range( N ) ];
    start = ( 0, 0 );
    visit[ 0 ][ 0 ] = [ 0, 0, 0, 0 ];
    
    dfs(  N, start, 0, 0 );

    
    dfs( N, start, 0, 1 );
    
    '''
    dfs( board, N, ( 0, 0 ), 0, 2 );

    
    dfs( board, N, ( 0, 0 ), 0, 3 );

    /*8'''
    
    
        
    return min( visit[ N - 1 ][ N - 1 ] );


solution( 	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]] );