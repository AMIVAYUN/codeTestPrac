# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:48:00 2022
@FileName: 11000.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11000
"""
#Time Out
def t1():
    
    def RoomCheck( rooms, case ):
        print( rooms, case )
        S,T,cost = case;
        flag = True;
        for idx in range( len( rooms ) ):
            
            if( rooms[ idx ] <= S ):
                rooms[ idx ] = T
                flag = False;
                break;
        if( flag ):
            rooms.append( T );
        
        return rooms;
            
    N = int( input() );
    
    lst = [];
    
    for i in range( N ):
        a, b = map( int, input().split() );
        
        lst.append( ( a, b, b - a ) );
        
        
    
    #lst = list( sorted( lst, key = lambda x: ( x[ 2 ], x[ 0 ], x[ 1 ] ) ) ) --> 4% WA
    lst = list( sorted( lst, key = lambda x: ( x[ 0 ], x[ 1 ], x[ 2 ] ) ) )
    
    
    Rooms = [];
    
    for i in range( N ):
        Rooms = RoomCheck( Rooms, lst[ i ] );
    
    print( len( Rooms ) )
    
# 4% TimeOut
def t2():
    N = int( input() );
    
    lst = [];
    
    for i in range( N ):
        a, b = map( int, input().split() );
        
        lst.append( ( a, b ) );
        
        
    
    #lst = list( sorted( lst, key = lambda x: ( x[ 2 ], x[ 0 ], x[ 1 ] ) ) ) --> 4% WA
    lst = list( sorted( lst, key = lambda x: ( x[ 0 ], x[ 1 ] ) ) )
    
    cnt = 0;
    
    while lst:
        start = lst.pop( 0 )[ 1 ]
        idx = 0;
        
        while idx < len( lst ):
            flag = True;
            if lst[ idx ][ 0 ] >= start:

                flag = False;
                start = lst[ idx ][ 1 ]
                lst.pop( idx );
                
            if( flag ):
                idx += 1;
            
        cnt += 1;
    
    print( cnt )
# 4% WA
def t3():
    import  bisect;
    N = int( input() );
    
    lst = [];
    
    for i in range( N ):
        a, b = map( int, input().split() );
        

        lst.append( ( a, b ) );
        
        
        
    cnt = 0;
    #lst = list( sorted( lst, key = lambda x: ( x[ 2 ], x[ 0 ], x[ 1 ] ) ) ) --> 4% WA
    lst = list( sorted( lst, key = lambda x: ( x[ 0 ], x[ 1 ] ) ) )
    rooms = [];
    for case in lst:
        
        idx = bisect.bisect_left( rooms, case[ 0 ] );
        
        print( rooms, idx, case )
        
        if( ( idx == len( rooms )  ) or ( idx == 0  and rooms[ idx ] > case[ 0 ] ) ):
            cnt += 1
            rooms.append( case[ 1 ] )
        
        else:
            rooms[ idx ] = case[ 1 ] 
        
        rooms = sorted( rooms )
    
    print( cnt )


from queue import PriorityQueue;

pq = PriorityQueue( [ 5,4,3 ] )


def t4():
    from queue import PriorityQueue;
    import bisect;
    rooms = PriorityQueue();
    
    N = int( input() );
    
    if ( N == 1 ):
        print( 1 );
        return;
        
    lst = [];
    
    for i in range( N ):
        a, b = map( int, input().split() );
        

        lst.append( ( a, b ) );
        
        
        
    cnt = 0;
    #lst = list( sorted( lst, key = lambda x: ( x[ 2 ], x[ 0 ], x[ 1 ] ) ) ) --> 4% WA
    lst = list( sorted( lst, key = lambda x: ( x[ 0 ], x[ 1 ] ) ) )
    
    rooms.put( lst[ 0 ][ 1 ] )
    
    for case in lst[1:]:
        
        for i in range( rooms.qsize() ):
            node = rooms.get();
            
            if( node <= case[ 0 ] ):
                rooms.put( case[ 1 ] );
                break
            else:
                rooms.put( node );
                rooms.put( case[ 1 ] );
        
    
    print( rooms.qsize() )
    
def t5():
    
    import heapq;
    N = int( input() );
    lst = [];
    
    for i in range( N ):
        a, b = map( int, input().split() );
        

        lst.append( ( a, b ) );
        
    lst = list( sorted( lst, key = lambda x: ( x[ 0 ], x[ 1 ] ) ) )
    
    rooms =  [ lst[ 0 ][ 1 ] ] 
    
    heapq.heapify( rooms );
    
    
 

    for i in range( 1, N ):
        if( rooms[ 0 ] > lst[ i ][ 0 ] ):
            heapq.heappush( rooms, lst[ i ][ 1 ] );
            
        else:
            heapq.heappop( rooms )
            heapq.heappush( rooms, lst[ i ][ 1 ] );
        
    print( len( rooms ) )
    
t5()