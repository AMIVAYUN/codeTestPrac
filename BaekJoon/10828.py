# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 20:00:55 2022
@FileName: 10828.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/10828
"""
N = int( input() );
class Stack:
    def __init__( self ):
        self.stack =  [];
        self.top = -1;
        self.dit = {"push": self.push, "pop": self.pop, "top": self.vtop, "size":self.size, "empty": self.isEmpty }
    
    def isEmpty( self ):
        return int( self.top == -1 );
    

    
    def push(self, i ):
        self.top += 1;
        self.stack.append( i );
        
    def pop( self ):
        if( self.isEmpty() ):
            return -1;
        val = self.stack[ self.top ];
        self.stack.pop();
        self.top -= 1;
        return val;
    
    def vtop( self ):
        if( self.top == -1 ):
            return -1
        return self.stack[ self.top ];
    
    def size( self ):
        return self.top + 1;
        
    def direct( self, message ):
        m = message.split();
        
        if( len( m ) > 1 ):
            self.dit[ m[ 0 ] ]( int( m[ 1 ] ) );
        
        else:
            
            print( self.dit[ m[ 0 ] ]() );

stack = Stack();

for i in range( N ):
    message = input();
    stack.direct( message ) ;
    print( stack.stack );
    

