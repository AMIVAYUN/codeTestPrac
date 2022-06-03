# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:36:25 2022
@FileName: stack.py
@author: YUNJUSEOK
"""



#LIFO

class Stack:
    def __init__ ( self ):
        self.content = []
        
    def __len__ ( self ):
        return len( self.content );
    
    def isEmpty( self ):
        if( len( self.content ) == 0 ):
            return True;
        else:
            return False;        
        
    def push( self, item ):
        self.content.append( item );
        
    def pop( self ):
        if( self.isEmpty() ):
            return False;
        return self.content.pop( -1 );
    
    def peek( self ):
        if( self.isEmpty() ):
            return False;
        return self.content[ -1 ];



def main():
    stack = Stack( );
    stack.push( 1 );
    print( stack.content );
    print( stack.pop() );
    

if( __name__ == "__main__"):
    main();

