# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 13:23:02 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


lenx, leny = 0, 0;

def shiftRow( rowc, colc ):
    from collections import deque;
    global lenx, leny;
    
    val = rowc.pop();
    
    rowc.appendleft( val );
    

    for idx in range( len( colc ) ):
        val = colc[ idx ].pop()
        colc[ idx ].appendleft( val );
    

    
    
    return rowc, colc;

def rotate( rowc, colc ):
    next = colc[ 0 ].popleft();
    
    rowc[ 0 ].appendleft( next );
    next = rowc[ 0 ].pop();
    
    colc[ -1 ].appendleft( next );
    next = colc[ -1 ].pop();
    
    rowc[ -1 ].append( next );
    next = rowc[ -1 ].popleft();

    
    colc[ 0 ].append( next );

    
    return rowc, colc;
   
def solution(rc, operations):
    global lenx, leny;
    from collections import deque;
    
    
    rowc = deque( [ deque( row [1:-1] ) for row in rc ] );
    
    lenx, leny = len( rc ), len( rc[ 0 ] );
    
    colc =  deque( [ deque( [ rc[ i ][ 0 ] for i in range( lenx ) ] ), deque( [ rc[ i ][ -1 ] for i in range( lenx ) ] ) ] )
    

    
    new_oper = [];
    idx = 0;
    
    #print( shiftRow( rowc, colc ) );
    #print( rotate( rowc, colc ) );
    
    for oper in operations:

        if( oper == 'ShiftRow' ):
            rowc, colc = shiftRow( rowc, colc );

        else:
            rowc, colc = rotate( rowc, colc );
                
    
    
    
    answer = [];
    for x in range( lenx ):
        answer.append( [ colc[ 0 ][ x ] ] + list( rowc[ x ] ) + [ colc[ -1 ][ x ] ] )
        #answer.append( list( colc[ 0 ][ x ] ) + [ rowc[ x ] ] + list( colc[ -1 ][ x ] ) );
    
    return answer;
    

#SOL1 WA

'''
def shiftRow( graph ):
    
    global lenx, leny;
    
    
    val = graph.pop();

    graph.appendleft( val );
    
    return graph;

def rowPush( start, x, graph ):
    global lenx, leny;

    
    val = graph[ x ].pop();
    graph[ x ].appendleft( start );
    
    return graph, val;
    
    
def rowPull( start, x, graph ):
    global lenx, leny;
 
    val = graph[ x ].popleft();
    
    sub = graph[ x ].pop() 
    graph[ x ].append( start )
    graph[ x ].append( sub );
    return graph, val;
    
    
def colPush( start, y, graph ):

    global lenx, leny;
    val = graph[ -1 ][ y ];
    for dx in range( 2,lenx ):
        graph[ dx ][ y ] = graph[ dx - 1 ][ y ];
    
    graph[ 1 ][ y ] = start;
    
    return graph, val;


def colPull( start, y, graph ):
    global lenx, leny;
    
    val = graph[ 0 ][ y ];
    for dx in range( lenx - 2 ):
        graph[ dx ][ y ] = graph[ dx + 1 ][ y ];
    
    graph[ lenx - 2 ][ y ] = start;
    
    return graph,val;
    

def Print( rc ):
    for row in rc:
        print( row )
def Rotate( graph ):
    global lenx, leny;
    next = graph[ 1 ][ 0 ];
 
    graph, next = rowPush( next, 0, graph )

    graph, next =colPush( next, leny - 1, graph)

    graph, next =rowPull( next, lenx - 1, graph );

    graph, next =colPull( next, 0, graph );

    return graph;
def solution(rc, operations):
    global lenx, leny;
    from collections import deque;
    
    
    rc = deque( [ deque( row ) for row in rc ] );
    lenx, leny = len( rc ), len( rc[ 0 ] );
    
    new_oper = [];
    idx = 0;

    for oper in operations:

        if( oper == 'ShiftRow' ):
            rc = shiftRow( rc );

        else:
            rc = Rotate( rc );
                

    
    answer = [];
    for x in range( lenx ):
        answer.append( list( rc[ x ] ) );
    return answer;
    
'''