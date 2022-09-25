# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:24:10 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""



dx = [ -1, 1, 0, 0 ];

dy = [ 0, 0, -1, 1 ];

'''
 바 0 0 0 | 1 1 1 | 2 2 2 | 3 3 3
 
사각형 perm( 0 1 2 3 )
11 3  

좌 우 상 하

0 1 2
0 1 3
'''
 

def getBar( direction, pos ):
    global graph,n,m;
    Mx = 0 ;
    x, y = pos;
    
    start = graph[ x ][ y ]

    for i in range( 3 ):
        nx = x + dx[ direction ];
        ny = y + dy[ direction ];
            
        if( 0<= nx < n and 0 <= ny < m ):
            x = nx
            y = ny
            start += graph[ nx ][ ny ];
            
        else:
            return 0;
        
   
    
    
    return start;
    
def getSquare( direction, pos ):
    global graph,n,m;
    dx2 = [ 0, -1, 0, 1 ]
    dy2 = [ 1, 0, -1, 0 ]
    Mx = 0;
    
    x, y = pos;
    start = 0
    for i in range( 4 ):

        direction = ( direction + 1 ) % 4;

        
        nx = x + dx2[ direction ];
        ny = y + dy2[ direction ];
        
        if( 0<= nx < n and 0 <= ny < m ):
            x = nx
            y = ny
            start += graph[ nx ][ ny ];
        
        else:
            return 0;
    
    
    return start;

def getL( direction,pos ):
    
    Mx = 0;
    x, y = pos;
    
    start = graph[ x ][ y ] 
    
    for i in range( 2 ):
        nx = x + dx[ direction ];
        ny = y + dy[ direction ];
        
        if( 0 <= nx < n and 0 <= ny < m ):
            x = nx
            y = ny;
            start += graph[ nx ][ ny ];
        else:
            return 0;
    
    if( direction == 0 ):
        nx1, ny1 = x + dx[ 2 ], y + dy[ 2 ]
        nx2, ny2 = x + dx[ 3 ], y + dy[ 3 ]
        if( 0<= nx1 < n and 0 <= ny1 < m ):
            val1 = graph[ nx1 ][ ny1 ]
        else:
            val1 = 0;
        
        if( 0<= nx2 < n and 0 <= ny2 < m ):
            val2 = graph[ nx2 ][ ny2 ]
        else:
            val2 = 0;
        
    elif( direction == 1 ):
        nx1, ny1 = x + dx[ 2 ], y + dy[ 2 ]
        nx2, ny2 = x + dx[ 3 ], y + dy[ 3 ]
        if( 0<= nx1 < n and 0 <= ny1 < m ):
            val1 = graph[ nx1 ][ ny1 ]
        else:
            val1 = 0;
        
        if( 0<= nx2 < n and 0 <= ny2 < m ):
            val2 = graph[ nx2 ][ ny2 ]
        else:
            val2 = 0;
    
    elif( direction == 2 ):
        nx1, ny1 = x + dx[ 0 ], y + dy[ 0 ]
        nx2, ny2 = x + dx[ 1 ], y + dy[ 1 ]
        if( 0<= nx1 < n and 0 <= ny1 < m ):
            val1 = graph[ nx1 ][ ny1 ]
        else:
            val1 = 0;
        
        if( 0<= nx2 < n and 0 <= ny2 < m ):
            val2 = graph[ nx2 ][ ny2 ]
        else:
            val2 = 0;
            
    else:
        nx1, ny1 = x + dx[ 0 ], y + dy[ 0 ]
        nx2, ny2 = x + dx[ 1 ], y + dy[ 1 ]
        if( 0<= nx1 < n and 0 <= ny1 < m ):
            val1 = graph[ nx1 ][ ny1 ]
        else:
            val1 = 0;
        
        if( 0<= nx2 < n and 0 <= ny2 < m ):
            val2 = graph[ nx2 ][ ny2 ]
        else:
            val2 = 0;
    
    
    Mx = max( val1, val2 )
    
    if( Mx ):
        return start + Mx;
    else:
        return 0;

def getThunder( direction, pos ):
    global graph,n,m;
    
    x, y = pos;
    
    nx = x + dx[ direction ];
    ny = y + dy[ direction ];
    start = graph[ x ][ y ]
    if( 0<= nx < n and 0<= ny < m ):
        start += graph[ nx ][ ny ]
        x, y = nx, ny;
    else:
        return 0;
    
    if( direction == 0 or direction == 1):
        nx1, ny1 = x + dx[ 2 ], y + dy[ 2 ]
        nx2, ny2 = x + dx[ 3 ], y + dy[ 3 ]
        if( 0<= nx1 < n and 0 <= ny1 < m ):
            val1 = graph[ nx1 ][ ny1 ]
        else:
            val1 = 0;
        
        if( 0<= nx2 < n and 0 <= ny2 < m ):
            val2 = graph[ nx2 ][ ny2 ]
        else:
            val2 = 0;
            
    else:
        nx1, ny1 = x + dx[ 0 ], y + dy[ 0 ]
        nx2, ny2 = x + dx[ 1 ], y + dy[ 1 ]
        if( 0<= nx1 < n and 0 <= ny1 < m ):
            val1 = graph[ nx1 ][ ny1 ]
        else:
            val1 = 0;
        
        if( 0<= nx2 < n and 0 <= ny2 < m ):
            val2 = graph[ nx2 ][ ny2 ]
        else:
            val2 = 0;
    
    if( val1 == val2 == 0 ):
        return 0;
    
    else:
        x1,y1 = nx1, ny1;
        x2,y2 = nx2, ny2;
        
        nx1,ny1 = x1 + dx[ direction ], y1 + dy[ direction ];
        nx2,ny2 = x2 + dx[ direction ], y2 + dy[ direction ];
        
        if( 0<= nx1 < n and 0<= ny1 < m ):
            rs1 = graph[ nx1 ][ ny1 ] + start + val1;
        else:
            rs1 = 0;
            
            
        if( 0<= nx2 < n and 0<= ny2 < m ):
            rs2 = graph[ nx2 ][ ny2 ] + start + val2;
        else:
            rs2 = 0;
        
        if( rs1 == rs2 == 0 ):
            return 0;
        elif( rs1 == 0 and rs2 > 0 ):
            return rs2;
        elif( rs1 > 0 and rs2 == 0 ):
            return rs1;
        else:
            return max( rs1, rs2 );
    
    return 0;

def getT( direction, pos ):
    global graph,n,m;
    import itertools;
    
    lst = { 0, 1, 2, 3 }
    x, y = pos;
    lst = lst - set( [ direction ] )
    start = graph[ x ][ y ]
    for number in lst:
        nx = x + dx [ number ];
        ny = y + dy [ number ]
        
        if( 0<= nx < n and 0<= ny < m ):
            start += graph[ nx ][ ny ];
        
        else:
            return 0;

    return start;
n, m = map( int ,input().split() );
Mx = 0;
graph = [];
for i in range( n ):
     graph.append( list( map( int, input().split() ) ) ) ;
                  
                  
                  
for i in range( n ):
    for j in range( m ):
        direction = 0;
        pos = ( i, j )
        for i in range( 4 ):
            direction = ( direction + 1 ) % 4;
            
            print( ( i, j ), [ Mx, getBar(direction, pos ), getL(direction, pos), getSquare(direction, pos),getT(direction, pos),getThunder(direction, pos)] )
            Mx = max( [ Mx, getBar(direction, pos ), getL(direction, pos), getSquare(direction, pos),getT(direction, pos),getThunder(direction, pos)])
                
        
        
        
        
print( Mx )