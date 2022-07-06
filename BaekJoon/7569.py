# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:50:40 2022
@FileName: 7569.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/7569
"""

'''
과거 로직:
    # -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:40:41 2022
@FileName: 7569.py
@author: YUNJUSEOK
@Link : https://www.acmicpc.net/problem/7569
"""


dx, dy = [ 0, 0, -1, 1 ], [ 1, -1, 0, 0 ]
M, N =  map( int, input().split() ) ;
farm = [];
for i in range( N ):
    farm.append( list( map( int, input().split() ) ) )
def main():
    global farm, M, N, dx, dy;
    from collections import deque;
    deq = deque([]);
    for i in range( N ):
        for j in range( M ):
            if( farm[ i ][ j ] == 1 ):
                deq.append( [ j, i ] );
    result = 0;
    while deq:
        dt = deq.popleft();
        x , y = dt[ 0 ], dt[ 1 ]
        for i in range( 4 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];

            if( -1 < nx < M and -1 < ny < N and farm[ ny ][ nx ] == 0):
                deq.append( ( nx, ny ) )
                farm[ ny ][ nx ] = farm[ y ][ x ] + 1;
    
    day = 0;

    for i in farm:
        for j in range( M ):
            if( i[j] == 0 ):
                
                return -1;
        day = max( day, max( i ) );
    
    
    return day - 1;

result = main()

print( result )


            

'''

'''
64% Out

"""
Created on Wed Jul  6 12:50:40 2022
@FileName: 7569.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/7569
"""

dx, dy, dz = [ 1, -1, 0, 0, 0, 0 ],[ 0, 0, 1, -1, 0, 0 ],[ 0, 0, 0, 0, 1, -1 ]

m, n, h = map( int, input().split() );
lst = [ [ [ 0 ] * m  for i in range( n ) ] for j in range( h ) ]
visit = [ [ [ 1 ] * m  for i in range( n ) ] for j in range( h ) ]
cnt = 0;
for i in range( h ):
    for j in range( n ):
        
        lst[ i ][ j ] = list( map( int, input().split() ) )
        cnt += lst[ i ][ j ].count( 0 );
        
from collections import deque;

deq = deque();



day = 0;
poscnt = 0;
while cnt and cnt != poscnt:
    # chk 1
    
    for i in range( h ):
        for j in range( n ):
            for k in range( m ):
                if( lst[ i ][ j ][ k ] == 1 and visit[ i ][ j ][ k ]):
                    visit[ i ][ j ][ k ] = 0;
                    deq.append( ( k, j, i ) );
    
    poscnt = cnt;
    
    while deq:
        
        x, y, z = deq.popleft();
        
        for i in range( 6 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];
            nz = z + dz[ i ];
            
            if( 0<= nx< m and 0<= ny < n and 0<= nz < h ):

                if( lst[ nz ][ ny ][ nx ] == 0 and visit[ nz ][ ny ][ nx ] ):
                    lst[ nz ][ ny ][ nx ] = 1;
                    cnt -= 1;
                
    
    
    day += 1;

print( day if not( cnt ) else -1 ) 
'''
from collections import deque;

dx, dy, dz = [ 1, -1, 0, 0, 0, 0 ],[ 0, 0, 1, -1, 0, 0 ],[ 0, 0, 0, 0, 1, -1 ]

m, n, h = map( int, input().split() );
lst = [ [ [ 0 ] * m  for i in range( n ) ] for j in range( h ) ]
visit = [ [ [ 1 ] * m  for i in range( n ) ] for j in range( h ) ]
cnt = 0;
deq = deque();

for i in range( h ):
    for j in range( n ):
        
        lst[ i ][ j ] = list( map( int, input().split() ) )
        cnt += lst[ i ][ j ].count( 0 );
        for k in range( m ):
            if( lst[ i ][ j ][ k ] == 1 ):
                visit[ i ][ j ][ k ] = 0;
                deq.append( ( k, j, i ) );
        





day = 0;
poscnt = 0;
while cnt and cnt != poscnt:
    # chk 1
    
    
    
    poscnt = cnt;
    newdeq = deque();
    while deq:
        
        x, y, z = deq.popleft();
        visit[ z ][ y ][ x ] = 0;
        for i in range( 6 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];
            nz = z + dz[ i ];
            
            if( 0<= nx< m and 0<= ny < n and 0<= nz < h ):

                if( lst[ nz ][ ny ][ nx ] == 0 and visit[ nz ][ ny ][ nx ] ):
                    newdeq.append( ( nx, ny, nz ) );
                    visit[ nz ][ ny ][ nx ] = 0;
                    lst[ nz ][ ny ][ nx ] = 1;
                    cnt -= 1;
                
    
    
    day += 1;
    deq = newdeq;
    

print( day if not( cnt ) else -1 ) 