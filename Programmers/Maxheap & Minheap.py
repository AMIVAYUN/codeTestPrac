# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:54:38 2022
@FileName: MaxHeap & MinHeap.py
@author: YUNJUSEOK
@Link:
"""

class MaxHeap:
    def __init__( self , items ):
        self.queue = [ None ] + items;
        for i in range( len( self.queue ) // 2 , 0, -1 ):
            self.max_heapify( i );
    
    def parent( self, index ):
        return index // 2 ;
    def leftchild( self, index ):
        return index * 2;
    
    def rightchild( self, index ):
        return index * 2 + 1;
    
    def swap( self, i, parent_index ):
        self.queue[ i ], self.queue[ parent_index ] = self.queue[ parent_index ], self.queue[ i ];
    
    def insert( self, n ):
        self.queue.append( n );
        for i in range( len( self.queue )//2, 0, -1):
            self.max_heapify( i );
        
    def delete( self ):
        last_index = len( self.queue ) - 1;
        if last_index == 0:
            return -1;
        self.swap( 1, last_index )
        max_value = self.queue.pop();
        self.max_heapify( 1 )
        return max_value;
    
    def max_heapify( self, i ):
        last_index = len( self.queue ) - 1;
        left_index = self.leftchild( i );
        right_index = self.rightchild( i );
        temp_max_index = i;
        
        if( left_index <= last_index and self.queue[ temp_max_index ] < self.queue[ left_index ] ):
            temp_max_index = left_index;
        if( right_index <= last_index and self.queue[ temp_max_index ] < self.queue[ right_index ] ):
            temp_max_index = right_index;
        if( temp_max_index != i ):
            self.swap( i, temp_max_index );
            self.max_heapify( temp_max_index );
    def print_heap(self):
        print(self.queue)

max_heap = MaxHeap([1,2])
max_heap.insert(1)
max_heap.insert(3)
max_heap.insert(5)
max_heap.print_heap()
print( max_heap.delete() )
max_heap.print_heap()

