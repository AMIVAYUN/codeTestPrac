# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:32:26 2022
@FileName: 19236.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/19236
"""
direction = [ None, ( -1, 0 ) , ( -1, -1 ), ( 0, -1 ), ( 1, -1 ), ( 1, 0 ), ( 1, 1 ), ( 0, 1 ), ( -1, 1 ) ]
n = 4;

fishpos = [ ( -1, -1 ) ] * 17; # -1, -1 더 이상 존재하지 않는다.
graph = [];
fishdirec = [ -1 ] * 17;

'''
fishpos = [(-1, -1), (1, 1), (0, 1), (1, 0), (2, 2), (3, 2), (2, 0), (0, 0), (3, 1), (0, 3), (1, 3), (2, 3), (3, 3), (2, 1), (1, 2), (0, 2), (3, 0)]
graph = [[7, 2, 15, 9], [3, 1, 14, 10], [6, 13, 4, 11], [16, 8, 5, 12]]
fishdirec = [-1, 8, 3, 1, 3, 2, 1, 6, 7, 8, 1, 4, 2, 6, 7, 6, 1]
'''
for x in range( n ):
    str0 = list( map( int, input().split() ) );

    str0 = [ ( str0[ i ], str0[ i + 1 ] ) for i in range( 0, 7, 2 ) ]
    
    row = [];
    for y in range( 4 ):
        fishpos[ str0[ y ][ 0 ] ] = ( x, y );
        fishdirec[ str0[ y ][ 0 ] ] = str0[ y ][ 1 ]; 
        row.append( str0[ y ][ 0 ] );
    graph.append( row );


init = graph[ 0 ][ 0 ];

graph[ 0 ][ 0 ] = 17;

fishpos[ init ] = ( -1, -1 );
shark = ( ( 0, 0 ), fishdirec[ init ], init );
fishdirec[ init ] = -1;

#print( shark, fishpos, fishdirec )
    
def getRefresh( graph, fishpos, fishdirec ):
    global direction;
    g = [ item[:] for item in graph ];
    fp = fishpos[:];
    fd = fishdirec[:];
    
    for fish in range( 1, 17 ):
        if( fp[ fish ][ 0 ] == -1 ):
            continue
        x, y = fp[ fish ];
        
        now_direc = fd[ fish ];
        
        for i in range( 8 ):
            nx, ny = x + direction[ now_direc ][ 0 ], y + direction[ now_direc ][ 1 ];
            if( 0<= nx < 4 and 0<= ny < 4 ):
                if( 0<= g[ nx ][ ny ]< 17 ):
                    if( g[ nx ][ ny ] == 0 ):
                        fp[ fish ] = ( nx, ny ); #빈칸이므로 채워주기
                        fd[ fish ] = now_direc;    
                        g[ nx ][ ny ] = fish;
                        g[ x ][ y ] = 0;
                        break;
                    else:
                        tg = g[ nx ][ ny ] # 타겟
                        g[ nx ][ ny ], g[ x ][ y ] = g[ x ][ y ], g[ nx ][ ny ]; #swap 해주고
                        fd[ fish ] = now_direc; # 방향 전환해주고
                        fp[ tg ], fp[ fish ] = fp[ fish ], fp[ tg ]; #위치 전환
                        break;
            now_direc = ( ( now_direc + 1 ) % 9 ) or 1
    
    return g,fp,fd;



def getResult( graph, fishpos, fishdirec, shark ):
    global direction;
    lst = [];
    
    Mx = shark[ 2 ];
    g_, fp_, fd_ = getRefresh(graph, fishpos, fishdirec);
    lst.append( ( shark, g_ ,fp_ , fd_ ) ); #연산 과정 -> 완전 탐색
    
    while lst:
        shark, g,fp,fd = lst.pop( 0 );
        
        sharkpos, sharkdirec, eatcnt = shark[ 0 ], shark[ 1 ], shark[ 2 ];
        
        for i in range( 1, 4 ):
            nx = sharkpos[ 0 ] + ( direction[ sharkdirec ][ 0 ] * i );
            ny = sharkpos[ 1 ] + ( direction[ sharkdirec ][ 1 ] * i );
            
            if( 0<= nx < 4 and 0<= ny < 4 ):
                if( 0 < g[ nx ][ ny ] < 17 ):
                    gtmp = [ item[:] for item in g ];
                    fptmp = fp[ : ];
                    fdtmp = fd[ : ];
                    tgtmp = g[ nx ][ ny ]
                    tempshark = ( ( nx, ny ), fd[ tgtmp ], eatcnt + tgtmp );
                    fdtmp[ tgtmp ] = -1;
                    fptmp[ tgtmp ] = ( -1, -1 );
                    gtmp[ sharkpos[ 0 ] ][ sharkpos[ 1 ] ] = 0;
                    gtmp[ nx ][ ny ] = 17;
                    '''
                    for alh in gtmp:
                        print( alh );
                    print( eatcnt + tgtmp, tempshark )
                    print( "-" * 25 )
                    '''
                    newg,newfp,newfd = getRefresh( gtmp, fptmp, fdtmp );
                    
                    lst.append( ( tempshark, newg, newfp, newfd ) );
                    
                    Mx = max( Mx, eatcnt + tgtmp );
                    
                    
        
    
    return Mx;
'''
for i in graph:
    print( i );
    
print( "-" * 25 )
'''
mx = getResult( graph, fishpos, fishdirec, shark );        
                        

print( mx )