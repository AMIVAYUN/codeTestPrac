# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:18:20 2023
@FileName: .py
@author: YUNJUSEOK
@Link:https://school.programmers.co.kr/learn/courses/30/lessons/87694?language=python3
"""




#sol2 배정밀도
def getRect( graph, rect ):
    xs = [ x for x in range( rect[ 0 ] * 2, rect[ 2 ] * 2 + 1 ) ];
    ys = [ y for y in range( rect[ 1 ] * 2, rect[ 3 ] * 2 + 1 ) ];
    
    Mnx, Mny = min( xs ), min( ys );
    Mxx, Mxy = max( xs ), max( ys );
    
    x_cor = [ Mnx, Mxx ]; y_cor = [ Mny, Mxy ];
    import itertools;
    prod = itertools.product;
    outside = list( prod( x_cor , ys ) ) + list( prod( xs, y_cor ) );

    for x, y in outside:
        if( graph[ x ][ y ] == 0 ):
            continue;
        
        graph[ x ][ y ] = 1;
        
    
    xs_ = [ x for x in range( rect[ 0 ] * 2 + 1, rect[ 2 ] * 2 ) ];
    ys_ = [ y for y in range( rect[ 1 ] * 2 + 1, rect[ 3 ] * 2 ) ]; 
    
    for x_, y_ in prod( xs_, ys_ ):
        graph[ x_ ][ y_ ] = 0;
    

    return graph;

def solution(rectangle, characterX, characterY, itemX, itemY):

    graph = [ [ 2 ] * 101 for _ in range( 101 ) ];


    rectangle = list( sorted( rectangle, key= lambda x: ( -( ( x[ 3 ] - x[ 1 ] + 1 ) * ( x[ 2 ] - x[ 0 ] + 1 )  ) ) ) );
    
    for rect in rectangle:
        graph = getRect( graph, rect );
    
    
    dx = [ 0, 0, 1, -1 ];
    dy = [ 1, -1, 0, 0 ];
    
    from collections import deque;
    
    rectangle = list( sorted( rectangle, key= lambda x: ( ( ( x[ 3 ] - x[ 1 ] + 1 ) * ( x[ 2 ] - x[ 0 ] + 1 )  ) ) ) );
    
    for rect in rectangle:
        graph = getRect( graph, rect );
    
    answer = 2501;
    start = ( characterX * 2, characterY * 2 );
    
    
    item = ( itemX * 2, itemY * 2 );
    
    
    dq = deque();
    
    visit = [ [ 10001  ] * 101 for _ in range( 101 ) ]
    
    visit[ start[ 0 ] ][ start[ 1 ] ] = 0;
    
    dq.append( ( 0, start ) )
    
    while dq:
        cnt, now = dq.popleft();
        
        
        if( cnt > answer ):
            continue;
            
        if( now == item ):
            answer = min( answer, cnt );
            continue;
        
        for i in range( 4 ):
            nx = now[ 0 ] + dx[ i ];
            ny = now[ 1 ] + dy[ i ];
            
            if( 0<= nx < 101 and 0<= ny < 101 ):
                if( graph[ nx ][ ny ] == 1 ):
                    if( visit[ nx ][ ny ] > cnt + 1 ):
                        visit[ nx ][ ny ] = cnt + 1;
                        dq.append( ( cnt + 1, ( nx, ny ) ) );
                    
        

    return answer //2;

'''

def getRect( graph, rect ):
    print( "rect: ", rect );
    xs = [ x for x in range( rect[ 0 ], rect[ 2 ] + 1 ) ];
    ys = [ y for y in range( rect[ 1 ], rect[ 3 ] + 1 ) ];
    
    Mnx, Mny = min( xs ), min( ys );
    Mxx, Mxy = max( xs ), max( ys );
    
    x_cor = [ Mnx, Mxx ]; y_cor = [ Mny, Mxy ];
    import itertools;
    prod = itertools.product;
    outside = list( prod( x_cor , ys ) ) + list( prod( xs, y_cor ) );
    
    for x, y in outside:
        if( graph[ x ][ y ] == 0 ):
            continue;
        
        graph[ x ][ y ] = 1;
        
    print( outside );

    xs_ = [ x for x in range( rect[ 0 ] + 1, rect[ 2 ] ) ];
    ys_ = [ y for y in range( rect[ 1 ] + 1, rect[ 3 ] ) ]; 
    
    print( list ( prod( xs_, ys_ ) ))
    for x_, y_ in prod( xs_, ys_ ):
        graph[ x_ ][ y_ ] = 0;

    for row in graph[:10]:
        print( row[:10] );
        
    print( "---" * 10 )
    
    return graph;

    초기 로직대로 가면 해당 그림 처럼 진행은하지만 1번케이스의 r 모형이 좌표가 겹쳐 방향을 정하지 못한다.
    
     1 1  에서 ㄷ 모양으로 가야하는데 바로 가버림.
     1 1 
     
     
     sol2 -> 배정밀도로 구현해보자 어차피 50 * 50 에서 100 * 100 되도 정사각형 4개 max라 40000개다.
    

    graph = [ [ 2 ] * 51 for _ in range( 51 ) ];
    rectangle 세로 1~4
    

    
    좌표값 항상 양수

    
    *직사각형이 최대 4개* 2500 * 4 == 10000
    

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [ [ 2 for k in range( 51 ) ]  for _ in range( 51 ) ];

    rectangle 세로 1~4
    
    좌표값 항상 양수

    
    *직사각형이 최대 4개* 2500 * 4 == 10000

    dx = [ 0, 0, 1, -1 ];
    dy = [ 1, -1, 0, 0 ];
    
    from collections import deque;
    
    rectangle = list( sorted( rectangle, key= lambda x: ( ( ( x[ 3 ] - x[ 1 ] + 1 ) * ( x[ 2 ] - x[ 0 ] + 1 )  ) ) ) );
    
    for rect in rectangle:
        graph = getRect( graph, rect );
    
    answer = 2501;
    start = ( characterX, characterY );
    
    
    item = ( itemX, itemY );
    
    
    dq = deque();
    
    visit = [ [ 2501  ] * 51 for _ in range( 51 ) ]
    
    visit[ start[ 0 ] ][ start[ 1 ] ] = 0;
    
    dq.append( ( 0, start ) )
    
    while dq:
        cnt, now = dq.popleft();
        
        
        if( cnt > answer ):
            continue;
            
        if( now == item ):
            answer = min( answer, cnt );
            continue;
        
        for i in range( 4 ):
            nx = now[ 0 ] + dx[ i ];
            ny =  + dy[ i ];
            
            if( 0<= nx < 51 and 0<= ny < 51 ):
                if( graph[ nx ][ ny ] == 1 ):
                    if( visit[ nx ][ ny ] > cnt + 1 ):
                        visit[ nx ][ ny ] = cnt + 1;
                        dq.append( ( cnt + 1, ( nx, ny ) ) );
                    
        
    print( answer );
    
    return answer

'''