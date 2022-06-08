# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:19:39 2022
@FileName: 3190.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/3190
"""
import sys;
'''
뱀이 있다 --> 1 
사과가 있다 --> -1
L D LEFT RIGHT
'''
#input = sys.stdin.readline;

dx = [ 1, 0,-1, 0 ]
dy = [ 0,1, 0, -1 ]
table = [];
move = {};
class snake:
    def __init__ ( self, apple, N ):
        self.dir = 0;
        self.pos = [0, 0]
        self.body = [ ( 0, 0 ) ]
        self.dxy = { 'L' : -1 , 'D' : 1}
        self.N = N;
        self.remain = apple;
        
    def changeDir( self, ch ):
        self.dir = ( self.dir + self.dxy[ ch ] ) % 4;
        
    def move( self, cnt ):
        global table, dx, dy,move;
        self.pos = [ self.pos[0] +  dx[ self.dir ], self.pos[ 1 ] +  dy[ self.dir ] ]
        x, y = self.pos[ 0 ], self.pos[ 1 ]
        if( x >= self.N or y >= self.N or x<0 or y< 0 or ( x, y ) in self.body ):
    
            return True;
        if( table[ y ][ x ] == -1 ):
            table[ y ][ x ] = 1
            self.body.append( ( x, y ) )
            self.remain -= 1;
            if( cnt in move ):
                self.changeDir( move[ cnt ] );
            
            return False;
            
        else:
            table[ y ][ x ] = 1;
            self.body.append( ( x, y ) )
            tail = self.body.pop( 0 );
            table [ tail[ 1 ] ][ tail[ 0 ] ] = 0;
            if( cnt in move ):
                self.changeDir( move[ cnt ] ) ;
            return False;
            
        
            
            
        
    

def main():
    global table, move,dx,dy;
    
    N = int( input() )
    
    table = [ [0] * N for _ in range( N ) ]
    table[ 0 ][ 0 ] = 1;
    
    K = int( input() );
    
    for i in range( K ):
        y, x = map( int, input().split() );
        table[ y - 1 ][ x - 1 ] = -1;
    M = int( input() );
    for i in range( M ):
        a, b = input().split();
        
        move[ int( a ) ] = b;
    sn1 = snake( K, N );  
    cnt = 0;
    while True: #K<0 이 아님.
        cnt += 1;
        if( sn1.move( cnt ) ):
            #print( cnt )
            break;
        
        
        
        
        
    print( cnt );
    
    
    return;


if( __name__ =="__main__"):
    main();

