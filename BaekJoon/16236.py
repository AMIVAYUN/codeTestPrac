# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 16:02:59 2022
@FileName: 16236.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/16236

문제 생기면 main 지울것 

"""
dx = [ 1, -1, 0, 0 ];
dy = [ 0, 0, -1, 1 ];
N = int( input() )
fish = [ 0 ] * 7;
class babyShark:
    def __init__( self,  pos  ):
        self.pos = pos;
        self.cnt = 0;
        self.size = 2;
        self.exp = 0;
    
    
    def chkEXP( self ):
        if( self.exp == self.size ):
            self.exp = self.exp % self.size;
            self.size += 1;
    
    def targeting2( self ):
        global graph,dx,dy,N;
        lst = [];
        Mx = N**2;
        pos = self.pos;
        target = ( Mx, pos, 2 );
        lst.append( ( pos, 0 ) )
        visit = [ [ 1 ] * ( N ) for _ in range( N ) ];
        visit[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
        while lst:
            pos, cnt = lst.pop( 0 );
            
            for i in range( 4 ):    
                nx = pos[ 0 ] + dx[ i ];
                ny = pos[ 1 ] + dy[ i ];
                
                if( 0 <= nx < N and 0 <= ny < N ):
                    if( graph[ nx ][ ny ] <= self.size and visit[ nx ][ ny ] ):
                        lst.append( ( ( nx, ny ), cnt + 1 ) )
                        visit[ nx ][ ny ] = 0;
                        if( 0 < graph[ nx ][ ny ] < self.size ):
                            if( target[ 0 ] > cnt + 1 ):
                                target = ( cnt + 1 , ( nx, ny ), graph[ nx ][ ny ]  );
                            elif( target[ 0 ] == cnt + 1 ):
                                pos_ = target[ 1 ];
                                if( pos_[ 0 ] < nx ):
                                    continue;
                                elif( pos_[ 0 ] == nx ):
                                    if( pos_[ 1 ] >= ny ):
                                        target = ( cnt + 1 , ( nx, ny ), graph[ nx ][ ny ]  );
                                else:
                                    target = ( cnt + 1 , ( nx, ny ), graph[ nx ][ ny ]  );
                                
        
        return target;
        
  
    def move( self, target ):
        global graph;
        movecnt, pos, fishsize = target[ 0 ], target[ 1 ], target[ 2 ];
        self.cnt += movecnt;
        graph[ self.pos[ 0 ] ][ self.pos[ 1 ] ] = 0;
        graph[ pos[ 0 ] ][ pos[ 1 ] ] = 9;
        self.pos = pos;
        self.fish[ fishsize -1 ] -= 1;
        self.exp += 1;
        self.chkEXP();
        
        return;

def main():
    global graph;
    graph = [];

    shark = babyShark( None );

    for i in range( N ):
        graph_ = list( map( int, input().split() ) );
        if( graph_.count( 9 ) ):
            idx = graph_.index( 9 );
            shark.pos = ( i, idx );
        for j in graph_:
            if( j > 6 ):
                continue
            fish[ j ] += 1;
        
        graph.append( graph_ );
    shark.fish = fish[ 1: ];


    while( sum( shark.fish ) > 0 ):
        target = shark.targeting2();

        if( target[ 0 ] == N**2 or target[ 1 ] == shark.pos ):
            break;
            
        shark.move( target );

        
        
    print( shark.cnt );



if( __name__ == "__main__" ):
    main();