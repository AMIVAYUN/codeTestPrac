# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:05:07 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


# -*- coding: utf-8 -*-
#REF
'''
def solution(commands):
    answer = []
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    board = [["EMPTY"] * 50 for _ in range(50)]
    for command in commands:
        command = command.split(' ')
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r,c,value = int(command[1])-1,int(command[2])-1,command[3]
                x,y = merged[r][c]
                board[x][y] = value
            elif len(command) == 3:
                value1, value2 = command[1], command[2]
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2
        elif command[0] == 'MERGE':
            r1,c1,r2,c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            x1,y1 = merged[r1][c1]
            x2,y2 = merged[r2][c2]
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2,y2):
                        merged[i][j] = (x1,y1)
        elif command[0] == 'UNMERGE':
            r, c = int(command[1])-1,int(command[2])-1
            x, y = merged[r][c]
            tmp = board[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x,y):
                        merged[i][j] = (i,j)
                        board[i][j] = "EMPTY"
            board[r][c] = tmp
        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            answer.append(board[x][y])
    return answer
'''

answer = [];
graph = [];
mapper = [];
def updateXY( cmd ):
    global answer, graph, mapper;
    x, y = int( cmd[ 0 ] ) - 1, int( cmd[ 1 ] ) -1;
    i, j = mapper[ x ][ y ];
    graph[ i ][ j ] = cmd[ 2 ];
  
    
    

def updateVal( cmd ):
    global answer, graph, mapper;
    
    for x in range( 50 ):
        for y in range( 50 ):
            if( graph[ x ][ y ] == cmd[ 0 ] ):
                graph[ x ][ y ] = cmd[ 1 ];
    
    

def merge( cmd ):
    global answer, graph, mapper;
    # ( x1, y1 ) > ( x2, y2 );

    x1, y1, x2, y2 = int( cmd[ 0 ] ) - 1, int( cmd[ 1 ] ) - 1, int( cmd[ 2 ] ) - 1, int( cmd[ 3 ] ) - 1;
    if( x1 == x2 and y1 == y2 ):
        return;
    
    p_x1, p_y1 = mapper[ x1 ][ y1 ];
    p_x2, p_y2 = mapper[ x2 ][ y2 ];
    
    val = graph[ p_x1 ][ p_y1 ][:]
    
    if( val == 'EMPTY' ):
        val = graph[ p_x2 ][ p_y2 ][:]
    
    graph[ p_x1 ][ p_y1 ] = val;
    

    target = mapper[ p_x2 ][ p_y2 ][:]
    for x in range( 50 ):
        for y in range( 50 ):
            if( mapper[ x ][ y ] == target ):

                mapper[ x ][ y ] = mapper[ p_x1 ][ p_y1 ];
     

    

def unmerge( cmd ):
    global answer, graph, mapper;
    x1, y1 = int( cmd[ 0 ] ) - 1, int( cmd[ 1 ] ) - 1;
    
   
    

    
    target = mapper[ x1 ][ y1 ][:];
    origin = graph[ target[ 0 ] ][ target[ 1 ] ][:];
    for x in range( 50 ):
        for y in range( 50 ):
            if( mapper[ x ][ y ] == target ):
                mapper[ x ][ y ] = ( x, y );
                graph[ x ][ y ] = "EMPTY";
    
    graph[ x1 ][ y1 ] = origin;
    
    

def Print( cmd ):
    global answer, graph, mapper;
    x1, y1 = int( cmd[ 0 ] ) - 1, int( cmd[ 1 ] ) - 1;
    x, y = mapper[ x1 ][ y1 ]
    answer.append( graph[ x ][ y ] );
    
    

def updateSelector( cmd ):
   
    if( len( cmd ) > 2 ):

        updateXY( cmd );
    else:

        updateVal( cmd );
    
def solution(commands):
    global answer, graph, mapper;
    from collections import defaultdict;

    
    mapper = [ [( j, i ) for i in range( 50 )] for j in range( 50 ) ]
    
    graph = [ [ "EMPTY" for _1 in range( 50 ) ] for _ in range( 50 )] 
    

    direc = { "UPDATE": updateSelector, "MERGE": merge, "UNMERGE": unmerge, "PRINT": Print };
    
    for command in commands:
        
        command = command.split();
        direction, cmd = command[ 0 ], command[ 1: ]
        
        direc[ direction ]( cmd )
        

        

    return answer;

"""
Created on Mon Apr  3 14:30:48 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
'''
#SOL1 RE 
answer = []
def updateXY( graph, mapper, group, valmapper , x, y , val ):
    strval = val[ : ];
    val = list( val );
    
    x, y = int( x ), int( y );
    x -= 1;
    y -= 1;
    parent_x, parent_y = mapper[ ( x, y ) ];
    
    graph[ parent_x ][ parent_y ] = val;
    valmapper[ strval ] = ( parent_x, parent_y ); 
    return graph,mapper,group, valmapper;

def merge( graph, mapper, group, valmapper, x1, y1, x2, y2 ):
    
    #우선권( x1, y1 );
    x1, y1, x2, y2 = int( x1 ), int( y1 ), int( x2 ), int( y2 );
    x1 -= 1;
    x2 -= 1;
    y1 -= 1;
    y2 -= 1;
    if( x1 == x2 and y1 == y2 ):
        return graph,mapper,group;
    parent_x1, parent_y1 = mapper[ ( x1, y1 ) ];
    parent_x2, parent_y2 = mapper[ ( x2, y2 ) ];    

    
    king , pawn = group[ ( parent_x1, parent_y1 ) ], group[ ( parent_x2, parent_y2 ) ];

    king.update( pawn );
    if( len( graph[ parent_x1 ][ parent_y1 ] ) ):
        for xc,yc in king:
            if( xc == parent_x1 and yc == parent_y1 ):
                continue;
            mapper[ ( xc, yc ) ] = ( parent_x1, parent_y1 );
            if( len( graph[ xc ][yc ] ) ):
                if( graph[ xc ][ yc ] != graph[ parent_x1 ][ parent_y1 ] ):
                    
                    valmapper.pop( ''.join( graph[ xc ][ yc ] ) );
            graph[ xc ][ yc ] = [];
            group[ (xc, yc ) ].add( ( parent_x1, parent_y1 ) );
                
            
        
        
        
        
       
    elif( len( graph[ parent_x2 ][ parent_y2 ] ) ):
        king , pawn = group[ ( parent_x1, parent_y1 ) ], group[ ( parent_x2, parent_y2 ) ];
        king.update( pawn );
        # 값 미리 빼오기
        origin = graph[ parent_x1 ][ parent_y1 ][:]
        graph[ parent_x1 ][ parent_y1 ] = graph[ parent_x2 ][ parent_y2 ][:];
        valmapper[ str( graph[ parent_x1 ][ parent_y1 ] ) ] = ( parent_x1, parent_y1 );
        valmapper.pop( origin );

        for xc, yc in king:
            if( xc == parent_x1 and yc == parent_y1 ):
                continue;
            mapper[ ( xc, yc ) ] = ( parent_x1, parent_y1 );
            if( len( graph[ xc ][yc ] ) ):
                if( graph[ xc ][ yc ] != graph[ parent_x1 ][ parent_y1 ] ):
                    
                    valmapper.pop( ''.join( graph[ xc ][ yc ] ) );
            graph[ xc ][ yc ] = [];
            group[ (xc, yc ) ].add( ( parent_x1, parent_y1 ) );
        
        
        
    else:
        king , pawn = group[ ( parent_x1, parent_y1 ) ], group[ ( parent_x2, parent_y2 ) ];
        king.update( pawn );
        
        for xc, yc in king:
            if( xc == parent_x1 and yc == parent_y1 ):
                continue;
            mapper[ ( xc, yc ) ] = ( parent_x1, parent_y1 );
            if( len( graph[ xc ][yc ] ) ):
                if( graph[ xc ][ yc ] != graph[ parent_x1 ][ parent_y1 ] ):
                    
                    valmapper.pop( ''.join( graph[ xc ][ yc ] ) );
            graph[ xc ][ yc ] = [];
            group[ (xc, yc ) ].add( ( parent_x1, parent_y1 ) );
        
    return  graph, mapper, group, valmapper

def updateVal(  graph, mapper, group, valmapper, val1, val2 ):
    parent_x1, parent_y1 = valmapper[ val1 ];
    
    graph[ parent_x1 ][ parent_y1 ] = list( val2 );
    
    valmapper.pop( val1 );
    
    valmapper[ val2 ] = ( parent_x1, parent_y1 );
    
    return  graph, mapper, group, valmapper;

def unmerge(  graph, mapper, group, valmapper, x1, y1 ):
    x1, y1 = int( x1 ),int( y1 );
    x1, y1 = x1 - 1, y1- 1 ;
    parent_x1, parent_y1 = mapper[ ( x1,y1 ) ]
    origin = [];
    
    if( len( graph[ parent_x1 ][ parent_y1 ] ) ):
        origin = graph[ parent_x1 ][ parent_y1 ][:];
        valmapper[ str( origin ) ] = ( x1, y1 ); 
    for xc, yc in group[ ( parent_x1, parent_y1 ) ]:
        if( xc == parent_x1 and yc == parent_y1 ):
            continue;
        graph[ xc ][ yc ] = [];
        mapper[ ( xc, yc ) ] = ( xc, yc );
        group[ ( xc, yc ) ] = ( xc, yc )
    
    graph[ x1 ][ y1 ] = origin;
    
    
    return graph, mapper, group, valmapper;
        
    
def Print( graph, mapper, group, valmapper, x1, y1 ):
    global answer
    x1, y1 = int( x1 ), int( y1 );
    x1 -= 1; y1 -= 1;
    parent_x1, parent_y1 = mapper[ ( x1, y1 ) ];
    
    if( len( graph[ parent_x1 ][ parent_y1 ] ) ):
        answer.append( ''.join( graph[ parent_x1 ][ parent_y1 ] ) );
    else:
        answer.append( "EMPTY" );
    
    return graph, mapper, group, valmapper

    
def solution(commands):
    global answer;

    
    from collections import defaultdict;
    
    graph = [ [ [] for y in range( 5 ) ] for x in range( 5 ) ]
    # A좌표가 가리키는 실제 지점
    mapper = defaultdict( tuple );
    # A좌표와 묶여있는 지점들
    group = defaultdict( set );
    
    valmapper = defaultdict( tuple );
    
    for x in range( 5 ):
        for y in range( 5 ):
            mapper[ ( x, y ) ] = ( x, y );
            group[ ( x, y ) ].add( ( x, y ) );
    
    for command in commands:
        
     

        cmdlst = command.split();
        graph, mapper, group, valmapper
        if( cmdlst[ 0 ] == 'UPDATE' ):
            if( len( cmdlst ) > 3 ):
                graph, mapper, group, valmapper = updateXY( graph, mapper, group, valmapper, cmdlst[ 1 ], cmdlst[ 2 ], cmdlst[ 3 ] );
            else:
                graph, mapper, group, valmapper = updateVal( graph, mapper, group, valmapper, cmdlst[ 1 ], cmdlst[ 2 ] );
        
        elif( cmdlst[ 0 ] == 'MERGE' ):
            graph, mapper, group, valmapper = merge( graph, mapper, group, valmapper, cmdlst[ 1 ], cmdlst[ 2 ], cmdlst[ 3 ], cmdlst[ 4 ] );
          
        elif( cmdlst[ 0 ] == 'UNMERGE' ):
            graph, mapper, group, valmapper = unmerge( graph, mapper, group, valmapper, cmdlst[ 1 ], cmdlst[ 2 ] );
        else:
            Print( graph, mapper, group, valmapper, cmdlst[ 1 ], cmdlst[ 2 ] );
            
    
      
    
    return answer


'''



