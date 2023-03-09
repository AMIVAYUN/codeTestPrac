# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:45:42 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
# 시간초과
dx = [ 1, -1, 0, 0 ];
dy = [ 0, 0, -1, 1 ];
StoLcnt = float( 'inf' );
LtoEcnt = float( 'inf' );
lenx, leny = 0, 0;
'''
# SOL1 DFS 시간 초과로 개선 여지가 없어 BFS로 넘어감.
def StoL( cnt, new_maps, pos,prev, counter ):
    global dx, dy, StoLcnt, lenx, leny;

    if( cnt > StoLcnt ):
        return;
    
    if( cnt > counter[ pos[ 0 ] ][ pos[ 1 ] ] ):
        return;

    if( new_maps[ pos[ 0 ] ][ pos[ 1 ] ] == 2 ):
        StoLcnt = cnt;
        return;

    counter[ pos[ 0 ] ][ pos[ 1 ] ] = cnt;
    
    for i in range( 4 ):
        newx = pos[ 0 ] + dx[ i ];
        newy = pos[ 1 ] + dy[ i ];

        if( 0<= newx < lenx and 0<= newy < leny ):

            if( prev == None or ( ( newx, newy ) != prev ) ):
        
                if( new_maps[ newx ][ newy ] != -1 ):
                    StoL( cnt + 1, new_maps, ( newx, newy ), pos, counter );
                    
def LtoE( cnt, new_maps, pos,prev, counter ):

    global dx, dy, LtoEcnt, lenx, leny;

    if( cnt > LtoEcnt ):
        return;
    
    if( cnt > counter[ pos[ 0 ] ][ pos[ 1 ] ] ):
        return;

    if( new_maps[ pos[ 0 ] ][ pos[ 1 ] ] == 3 ):
        LtoEcnt = cnt;
        return;

    counter[ pos[ 0 ] ][ pos[ 1 ] ] = cnt;
    
    for i in range( 4 ):
        newx = pos[ 0 ] + dx[ i ];
        newy = pos[ 1 ] + dy[ i ];

        if( 0<= newx < lenx and 0<= newy < leny ):

            if( prev == None or ( ( newx, newy ) != prev ) ):
        
                if( new_maps[ newx ][ newy ] != -1 ):
                    LtoE( cnt + 1, new_maps, ( newx, newy ), pos, counter );
        
def solution(maps):
    pos = 0;
    Lpos = 0;
    answer = 0;
    new_maps= [];
    global lenx, leny, StoLcnt, LtoEcnt;
    lenx, leny = len( maps ), len( maps[ 0 ] );
    for x in range( lenx ):
        temp = [];
        for y in range( leny ):
            if( maps[ x ][ y ] == 'S' ):
                pos = ( x, y );
                temp.append( 1 );
            elif( maps[ x ][ y ] == 'O' ):
                temp.append( 0 );
            elif( maps[ x ][ y ] == 'X' ):
                temp.append( -1 );
            elif( maps[ x ][ y ] == 'L' ):
                Lpos = ( x, y );
                temp.append( 2 );
            else:
                temp.append( 3 );
        new_maps.append( temp );
    counter = [ [ float('inf') for y in range( leny ) ] for x in range( lenx ) ];
    counter[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
    StoL( 0, new_maps, pos, None , counter );
    
    if( StoLcnt == float('inf') ):
        return -1;
    
    else:
        answer += StoLcnt;
    counter = [ [ float('inf') for y in range( leny ) ] for x in range( lenx ) ];
    counter[ Lpos[ 0 ] ][ Lpos[ 1 ] ] = 0;
    
    LtoE( 0, new_maps, Lpos, None, counter );
    
    if( LtoEcnt == float( 'inf' ) ):
        return -1;
    
    else:
        return answer + LtoEcnt
    

'''
dx = [ 1, -1, 0, 0 ];
dy = [ 0, 0, -1, 1 ];
StoLcnt = float( 'inf' );
LtoEcnt = float( 'inf' );
lenx, leny = 0, 0;
from collections import deque;
def makeCounter( lenx, leny, pos ):
    counter = [ [ float('inf') for y in range( leny ) ] for x in range( lenx ) ];
    counter[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
    return counter;

def bfs( lenx, leny, start, end, maps, obj):
    deq = deque();
    counter = makeCounter( lenx,leny, start );
    deq.append( ( start, 0) );
    while deq:
        pos, cnt = deq.popleft();

        x, y = pos[ 0 ], pos[ 1 ];
        
        
        
        if( maps[ x ][ y ] == obj ):
            counter[ x ][ y ] = min( counter[ x ][ y ], cnt );
            continue;

        
        for i in range( 4 ):
            newx = x + dx[ i ];
            newy = y + dy[ i ];
            if( 0<= newx < lenx and 0<= newy < leny ):
                if( maps[ newx ][ newy ] != 'X' ):
                    if( counter[ newx ][ newy ] > cnt + 1 and counter[ end[ 0 ] ][ end[ 1 ] ] > cnt + 1 ):
                        #counter[ end[ 0 ] ][ end[ 1 ] ] > cnt + 1 추가로 해결
                        counter[ newx ][ newy ] = min( counter[ newx ][ newy ], cnt + 1 );
                        deq.append( ( ( newx, newy ), cnt + 1 ) );

    return counter[ end[ 0 ] ][ end[ 1 ] ] if counter[ end[ 0 ] ][ end[ 1 ] ] != float('inf') else -1;
def check( pos, maps, lenx, leny ):
    global dx, dy;
    x,y = pos;
    for i in range( 4 ):
        nx = x + dx[ i ];
        ny = y + dy[ i ];
        
        if( 0<= nx < lenx and 0<= ny < leny ):
            if( maps[ nx ][ ny ] != 'X' ):
                return True;
    
    return False;
        
def solution(maps):
    global dx, dy;
    
    answer = 0;
    lenx, leny = len( maps ), len( maps[ 0 ] );
    Spos, Lpos, Epos = 0, 0, 0;
    for x in range( len( maps ) ):
        for y in range( len( maps[ 0 ] ) ):
            if( maps[ x ][ y ] == 'L' ):
                Lpos = ( x, y );
            elif( maps[ x ][ y ] == 'S' ):
                Spos = ( x, y );
            elif( maps[ x ][ y ] == 'E' ):
                Epos = ( x, y );
    
    if( check( Spos, maps, lenx, leny ) == False or check( Epos, maps, lenx, leny ) == False or check( Lpos, maps, lenx, leny ) == False ):
        return -1;
    
    Lcnt = bfs( lenx, leny, Spos, Lpos, maps, 'L')
    if( Lcnt == -1 ):
        return -1;
    
    answer += Lcnt;
    
    Ecnt = bfs( lenx, leny, Lpos, Epos, maps, 'E' );
    
    if( Ecnt == -1 ):
        return -1;
    
    return answer + Ecnt;
    
'''

def StoL( cnt, new_maps, pos,prev, counter ):
    global dx, dy, StoLcnt, lenx, leny;

    if( cnt > StoLcnt ):
        return;
    
    if( cnt > counter[ pos[ 0 ] ][ pos[ 1 ] ] ):
        return;

    if( new_maps[ pos[ 0 ] ][ pos[ 1 ] ] == 2 ):
        StoLcnt = cnt;
        return;

    counter[ pos[ 0 ] ][ pos[ 1 ] ] = cnt;
    
    for i in range( 4 ):
        newx = pos[ 0 ] + dx[ i ];
        newy = pos[ 1 ] + dy[ i ];

        if( 0<= newx < lenx and 0<= newy < leny ):

            if( prev == None or ( ( newx, newy ) != prev ) ):
        
                if( new_maps[ newx ][ newy ] != -1 ):
                    StoL( cnt + 1, new_maps, ( newx, newy ), pos, counter );
                    
def LtoE( cnt, new_maps, pos,prev, counter ):

    global dx, dy, LtoEcnt, lenx, leny;

    if( cnt > LtoEcnt ):
        return;
    
    if( cnt > counter[ pos[ 0 ] ][ pos[ 1 ] ] ):
        return;

    if( new_maps[ pos[ 0 ] ][ pos[ 1 ] ] == 3 ):
        LtoEcnt = cnt;
        return;

    counter[ pos[ 0 ] ][ pos[ 1 ] ] = cnt;
    
    for i in range( 4 ):
        newx = pos[ 0 ] + dx[ i ];
        newy = pos[ 1 ] + dy[ i ];

        if( 0<= newx < lenx and 0<= newy < leny ):

            if( prev == None or ( ( newx, newy ) != prev ) ):
        
                if( new_maps[ newx ][ newy ] != -1 ):
                    LtoE( cnt + 1, new_maps, ( newx, newy ), pos, counter );
        
def solution(maps):
    pos = 0;
    Lpos = 0;
    answer = 0;
    new_maps= [];
    global lenx, leny, StoLcnt, LtoEcnt;
    lenx, leny = len( maps ), len( maps[ 0 ] );
    for x in range( lenx ):
        temp = [];
        for y in range( leny ):
            if( maps[ x ][ y ] == 'S' ):
                pos = ( x, y );
                temp.append( 1 );
            elif( maps[ x ][ y ] == 'O' ):
                temp.append( 0 );
            elif( maps[ x ][ y ] == 'X' ):
                temp.append( -1 );
            elif( maps[ x ][ y ] == 'L' ):
                Lpos = ( x, y );
                temp.append( 2 );
            else:
                temp.append( 3 );
        new_maps.append( temp );
    counter = [ [ float('inf') for y in range( leny ) ] for x in range( lenx ) ];
    counter[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
    StoL( 0, new_maps, pos, None , counter );
    
    if( StoLcnt == float('inf') ):
        return -1;
    
    else:
        answer += StoLcnt;
    counter = [ [ float('inf') for y in range( leny ) ] for x in range( lenx ) ];
    counter[ Lpos[ 0 ] ][ Lpos[ 1 ] ] = 0;
    
    LtoE( 0, new_maps, Lpos, None, counter );
    
    if( LtoEcnt == float( 'inf' ) ):
        return -1;
    
    else:
        return answer + LtoEcnt
    
'''
solution( ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"] )