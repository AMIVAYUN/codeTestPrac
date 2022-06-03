# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:06:46 2022
@FileName: queue.py
@author: YUNJUSEOK
"""
import copy;
#FIFO
class Queue:
    def __init__( self ):
        self.content = [];
        
    def isEmpty( self ):
        return len( self.content ) == 0
    
    def enqueue( self ,item ):
        self.content.append( item );
    
    def dequeue( self ):
        if( self.isEmpty() ):
            raise Exception( "비어 있습니다. " );
        return self.content.pop( 0 );
    
    def peek( self ):
        if( self.isEmpty() ):
            raise Exception( "비어 있습니다. " );
        return self.content[ 0 ];

class CircleQueue:
    def __init__( self , size):
        self.content = [ 0 ] * size;
        self.front = 0;
        self.rear = 0;
        self.size = size;
    
    def isEmpty( self ):
        return self.front == self.rear;
    
    def isFull( self ):
        return self.front == ( self.rear + 1 ) % self.size
    
    def enqueue( self, item ):
        if( self.isFull() ):
            raise Exception( "사이즈를 넘었습니다. " );
        self.content[ self.rear ] = item;
        self.rear = ( self.rear +1 ) % self.size ;
    
    def dequeue( self ):
        if( self.isEmpty() ):
            raise Exception( "비어 있습니다. " );
        item = copy.deepcopy( self.content[ self.front ] );
        self.content[ self.front ] = 0;
        self.front = ( self.front + 1 ) % self.size;
        return item;
    def peek( self ):
        if( self.isEmpty() ):
            raise Exception( " 비어 있습니다 " );
        return self.content[ self.front ];

class Deque:
    def __init__( self, size ):
        self.content = [ 0 ] * size;
        self.front = 0;
        self.rear = 1;
        self.size = size;
    
    def isEmpty( self ):
        return self.front == self.rear;        
    
    
    def isFull( self ):
        return self.front == ( self.rear + 1 ) % self.size
    
    def add_rear( self, item ):
        if( self.isFull() ):
            raise Exception( "사이즈를 넘었습니다. " );
        self.content[ self.rear ] = item;
        self.rear = ( self.rear + 1 ) % self.size;
    
    def delete_rear( self ):
        if( self.isEmpty() ):
            raise Exception( " 비어 있습니다. " );
        
        self.rear = ( self.rear - 1 + self.size ) % self.size;
        item = copy.deepcopy( self.content[ self.rear ] );
        self.content[ self.rear ] = 0;
        return item;
    
    def get_rear( self ):
        if( self.isEmpty() ):
            raise Exception(" 비어 있습니다. ");
        return self.content[ ( self.rear -1 +self.size ) % self.size ];
    
    def add_front( self, item ):
        if( self.isFull() ):
            raise Exception( " 사이즈를 넘었습니다 " );
        self.content[ self.front ] = item;
        self.front = ( self.front - 1 + self.size ) % self.size;
    
    def delete_front( self ):
        if( self.isEmpty() ):
            raise Exception( " 비어 있습니다. " );
        self.front = ( self.front + 1 ) % self.size;
        item = copy.deepcopy( self.content[ self.front ] );
        self.content[ self.front ] = 0;
        return item;
    def get_front( self ):
        if( self.isEmpty() ):
            raise Exception( " 비어 있습니다. ")
        return self.content[ ( self.front - 1 + self.size) % self.size ];
    
        
def main():
    queue = Queue();
    '''
    for i in range( 10 ):
        queue.enqueue( i );
        
    print ( queue.content ); 
    for i in range( 10 ):
        print ( queue.dequeue()) ;
    '''    
    '''
    cqueue = CircleQueue( 11 );
    
    for i in range( 10 ):
        cqueue.enqueue( i );
        print( "rear: ", cqueue.rear );
    print( cqueue.content );
    print(" peek: ",cqueue.peek() );
    for i in range( 10 ):
        print ( cqueue.dequeue() );
        print( "front: ", cqueue.front );
    print( cqueue.content );
    '''
    dq = Deque( 10 );
    dq.add_front( 1 );
    print( dq.content, dq.front, dq.get_front() )
    dq.add_rear( 1 );
    dq.get_rear()
    print( dq.content, dq.rear ,dq.get_rear() )
if( __name__ == "__main__" ):
    main();
