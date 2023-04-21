# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:39:18 2023
@FileName: 17140.py
@author: YUNJUSEOK
@Link:
"""

'''
크기가 3×3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.

R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 
그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 
 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.

예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다. 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다.
 다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.

정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다.
 R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고,
 C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다. 
 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬할 때 0은 무시해야 한다. 
 예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.

행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.

배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.

수의 등장 횟수가 커지는 순.-> 수가 커지는 순

'''
def R( flag, graph ):
    from collections import defaultdict;
    
    #for rr in graph:
     #   print( rr );
    
    #print( '-')
    if flag:
        graph = list( zip( *graph ) );
        #print( '--changed' );
    #print('-')
    #for ro in graph: print( ro );
    #print('-')
    mXleng = 0;
    new_graph = [];
    for x in range( len( graph ) ):
        
        ddit = defaultdict( int );
        
        for y in range( len( graph[ x ] ) ):
            if( graph[ x ][ y ] == 0 ):
                continue;
            ddit[ graph[ x ][ y ] ] +=1;
        
            
        items = ddit.items();
        
        
        items = list( sorted( items, key = lambda x: ( x[ 1 ], x[ 0 ] )  ) )
        leng = len( items ) * 2;
        
        lst = [];
        
        for key, val in items:
            lst += [ key, val ];
        
        new_graph.append( lst );
        
        mXleng = max( mXleng, leng )
    
    #print("after-")
    
    #for ro in new_graph: print( ro );
    
    for i in range( len( new_graph ) ) :
        
        new_graph[ i ] += ( mXleng - len( new_graph[ i ] ) ) * [ 0 ];
        
        new_graph[ i ] = new_graph[ i ][ : 100 ];
        
    
    #print( "after2- ")
    #for ro in new_graph: print( ro );
        
    #for ro in graph: print( ro );
    
    #print( "-" )
    return list( zip( *new_graph ) ) if flag else new_graph;
graph =[]     
        
def main():
    global graph;
    r, c, k = map(int, input().split())
    r -= 1;
    c -= 1;
    
    row = 3; col= 3;
    graph = [];
    from collections import defaultdict;
    
    for i in range( 3 ):
        graph.append( list( map( int, input().split() ) ) );
    
        
    cnt = 0;
    
    while cnt < 100:
        
        
        #for ro in graph: print( ro );
        row = len( graph ); col = len( graph[ 0 ] ) 
        if( 0<= r < row and 0<= c < col and graph[ r ][ c ] == k) :
            break;
        
       
        graph = R( row < col,graph );
        cnt += 1;
    
    print( cnt if 0<= r < len( graph ) and 0<= c < len( graph[ 0 ] ) and graph[ r ][ c ] == k else -1 );
    
'''
SOL2 WA
def R( flag, row, col, graph, r, c ):
    from collections import defaultdict;
    
    if not flag:
        graph = list( zip( *graph ) );
        
        row, col = col, row;
        r, c = c, r;
    
    #for rr in graph:
     #   print( rr );
    
    #print( '-')
    minleng = 0;
    for x in range( len( graph ) ):
        
        ddit = defaultdict( int );
        
        for y in range( len( graph[ x ] ) ):
            ddit[ graph[ x ][ y ] ] +=1;
        
            
        items = ddit.items();
        
        
        items = list( sorted( items, key = lambda x: ( x[ 1 ], x[ 0 ] )  ) )
        leng = len( items ) * 2;
        
        lst = [];
        
        for key, val in items:
            lst += [ key, val ];
        
        graph[ x ] = lst[:100];
        
        minleng = max( minleng, leng )
        
    col = minleng;
    
    for x in range( row ):
        graph[ x ] += ( col - len( graph[ x ] ) ) * [ 0 ];
        
    
    return ( row, col, graph, r,c );
        
        
def main():
    r, c, k = map(int, input().split())
    r -= 1;
    c -= 1;
    
    row = 3; col= 3;
    graph = [];
    from collections import defaultdict;
    
    for i in range( 3 ):
        graph.append( list( map( int, input().split() ) ) );
    
        
    cnt = 0;
    
    while cnt < 100:
        if( 0<= r < row and 0<= c < col and graph[ r ][ c ] == k):
            break;
        
        row,col,graph, r,c = R( row >= col, row, col, graph, r,c );
        cnt += 1;
    
    print( cnt if graph[ r ][ c ] == k else -1 );
    
'''
'''
#SOL 1
def R( flag, row, col, graph,graphc ):
    from collections import defaultdict;
    stan = row if flag else col;
    print( flag )
    
    for x in range( stan ):
        ddit = defaultdict( int );
        
        if flag:
            if( graph[ x ][ 99 ] != 0 ):
                continue;
            for y in range( col ):
                ddit[ graph[ x ][ y ] ] +=1;
                graphc[ y ][ x ] = 0;
            
            graph[ x ] = [ 0 ] * 100;
        else:
            if( graphc[ x ][ 99 ] != 0 ):
                continue;
            for y in range( row ):
                ddit[ graphc[ x ][ y ] ] +=1;
                graph[ y ][ x ] = 0;
            
            graphc[ x ] = [ 0 ] * 100;
        
            
        nowleng = len( list( ddit.keys() ) ) * 2;
        
        
        stan = max( stan, nowleng );
        case = list( sorted( ddit.items(), key = lambda x: ( x[ 1 ], x[ 0 ] ) ) );
        leng = len( case );
        idxbias = 0;
        if flag:
            for i in range( 0, leng ):
                if( idxbias == 100 ):
                    break;
                graph[ x ][ idxbias ] = case[ i ][ 0 ];
                graph[ x ][ idxbias + 1 ] = case[ i ][ 1 ];
                    
                graphc[ idxbias ][ x ] = case[ i ][ 0 ];
                graphc[ idxbias + 1 ][ x ] = case[ i ][ 1 ];    
                    
                idxbias += 2;
            
            
            
        else:
            for i in range( 0, leng ):
                if( idxbias == 100 ):
                    break;
                graphc[ x ][ idxbias ] = case[ i ][ 0 ];
                graphc[ x ][ idxbias + 1 ] = case[ i ][ 1 ];
                    
                graph[ idxbias][ x ] = case[ i ][ 0 ];
                graph[ idxbias+ 1 ][ x ] = case[ i ][ 1 ];
                idxbias += 1;
            
                    

    return ( max( row, stan ), col, graph, graphc ) if flag else ( row, max( col, stan ) , graph,graphc );
        
def main():
    row , col = 3, 3;
    
    r,c,k = map( int, input().split() );
    r -= 1; c -= 1;
    
    graph = [ [ 0 ] * 100 for _ in range( 100 ) ];
    graphc = [ [ 0 ] * 100 for _ in range( 100 ) ];
    
    
    for x in range( 3 ):
        tc = list( map( int, input().split() ) );
        
        
        for y in range( 3 ):
            graph[ x ][ y ] = tc[ y ];     
            graphc[ y ][ x ] = tc[ y ]; 
    
    for l in graph[:3]:
        print( l[ :3 ]);
        
    
    
    for l_ in graphc[ :3 ]:
        print( l_[ :3] );
        
        
    print( "- - -")   
    cnt = 0;

    row, col, graph, graphc = R( row >= col, row, col, graph, graphc );
    
    for rr in graph[:6]:
        print( rr[:6] );

    #row,col,graph = R( row,col,graph );
    
    while cnt < 3 or graph[ r ][ c ] == k:
       
        row, col, graph,graphc = R( row>=col, row,col,graph, graphc );
        
        print( row , col );
        
        for rr in graph[ :10 ]:
            print( rr[ :10 ] );
            
        for rr in graphc[ : 10 ]:
            print( rr[ : 10 ] );
        
        cnt += 1;
'''

    
    #return cnt if graph[ r ][ c ] == k else -1;





if( __name__=="__main__" ):
    main();    

