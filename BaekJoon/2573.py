# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:10:56 2022
@FileName: 2573.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2573
"""
def dfs( x, y ):
    global visited, lst, X, Y, dx, dy;
    visited [ y ][ x ] = 0;

    for i in range( 4 ):
        nx = x + dx[ i ];
        ny = y + dy[ i ];
        if( 0<= nx <= X and 0<= ny <= Y ):
            if( visited[ ny ][ nx ] != 0):
                dfs( ny, nx );
    
    return;

def getlist():
    global Y,X,lst;
    result = [ [0] * X for i in range( Y ) ];
    for y in range( Y ):
        for x in range( X ):
            if( lst[ y ][ x ] ):
                result[ y ][ x ] = getCnt( x, y );
    
    return result;

def getCnt( x, y ):
    global lst, dx, dy;
    cnt = 0;
    for i in range( 4 ):
        nx = x + dx[ i ];
        ny = y + dy[ i ];
        if( 0<= nx <= X and 0<= ny <= Y ):
            if( not( lst[ ny ][ nx ] ) ):
                cnt+=1;
    
    return cnt;


Y,X = map( int, input().split() );
lst = [];
visited = [ [1] * X for i in range( Y ) ]

dx, dy = [ 0, 0, 1, -1 ], [ 1, -1, 0, 0 ]

def bfs( x, y ):
    global visited, lst, X, Y, dx, dy;
    from collections import deque;
    deq = deque();
    deq.append( ( x, y ) );
  
    
    while deq:
        pos = deq.popleft();
        for i in range( 4 ):
            nx = pos[0] + dx[ i ];
            ny = pos[1] + dy[ i ];
            if( 0<= nx <= X and 0<= ny <= Y ):
                if( visited[ ny ][ nx ]  ):
                    visited[ ny ][ nx ] = 0;
                    deq.append( (nx, ny) );

        
            
        
        
for i in range( Y ):
    lst.append( list( map( int, input().split() ) ) ) 
def main():
    
    global visited, lst, X, Y;
    cnt = 0;
    year = 0;

    while( True ):
        Ocount = 0;
        
        cnt = 0;
        year += 1;
        thisyear = getlist();
        for y in range( Y ):
            for x in range( X ):
                
                lst[ y ][ x ] = lst[ y ][ x ] - thisyear[ y ][ x ] if lst[ y ][ x ] >= thisyear[ y ][ x ] else 0;
                if( not( lst[ y ][ x ] ) ):
                    Ocount+=1;
                    visited[ y ][ x ] = 0;
                    
     
        
        for y in range( Y ):
            for x in range( X ):
                if( visited[ y ][ x ] ):
                    cnt += 1;
                    if( cnt >= 2 ):
                        print( year );
                        return;
                    visited[ y ][ x ] = 0;
                    bfs( x, y );
                    
                    
        if( Ocount == Y * X  ):
          
            print( 0 );
            return;
        
        visited = [ [1] * X for i in range( Y ) ]
        
        
            
    
    


if( __name__ == "__main__"):
    main();