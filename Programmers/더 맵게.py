# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:30:15 2022
@FileName: 더 맵게.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/42626
"""

def getscoville( x, y ):
    return x + ( y * 2 );
def insertion( lst , x ):
    if lst:
        lenx = len( lst );
        if( lst [ 0 ] < x ):
            return [ x ] + lst;
        for i in range( lenx -1 , -1, -1 ):
            if( lst[ i ] > x ):
                lst = lst[ : i + 1 ] + [ x ] + lst[ i + 1 : ];
                return lst;
            elif( i == 0 ):
                lst = [ x ] + lst;
                return lst;
    else:
        return [ x ];
        
    
def solution1(scoville, K):
    cnt = 0;
    scoville = sorted( scoville ,reverse = True )
    while len( scoville) > 1 and  scoville[ len( scoville ) - 1] < K:
        
        
        x, y = scoville.pop(), scoville.pop();
        sc = getscoville( x, y );
        
        cnt += 1;
 
        scoville = insertion( scoville, sc );
        
    if( len( scoville ) and min( scoville ) >= K ):
        return cnt;
    
    else:
        return -1;
    
            
            
            
class MinHeap:
    def __init__( self, items ):
        self.queue = [ None ] + items;
        for i in range( len( self.queue ) // 2, 0, -1 ):
            self.min_heapify( i );
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
        for i in range( len( self.queue ) //2 , 0 , -1 ):
            self.min_heapify( i );
    def delete( self ):
        last_index = len( self.queue ) -1;
        if( last_index == 0 ):
            return -1;
        self.swap( 1, last_index );
        min_value = self.queue.pop();
        self.min_heapify( 1 );
        return min_value;
    def min_heapify( self, i ):
        last_idx = len( self.queue ) -1;
        left_idx = self.leftchild( i );
        right_idx = self.rightchild( i );
        temp_min_idx = i;
        
        if( left_idx <= last_idx and self.queue[ temp_min_idx] > self.queue[ left_idx ] ):
            temp_min_idx = left_idx;
        if( right_idx <= last_idx and self.queue[ temp_min_idx ] > self.queue[ right_idx ] ):
            temp_min_idx = right_idx;
        if( temp_min_idx != i ):
            self.swap( i, temp_min_idx );
            self.min_heapify( temp_min_idx );
    def print_heap(self):
        print(self.queue)        

def getscoville( x, y ):
    return x + ( y * 2 );
    
def solution2(scoville, K):
    Mnh = MinHeap( scoville );
    answer = 0
    while(len( Mnh.queue ) > 2 and Mnh.queue[ 1 ] < K ):
        val1,val2 = Mnh.delete(),Mnh.delete();
        sc = getscoville( val1, val2 );
        Mnh.insert( sc );
        answer += 1;
    if( len( Mnh.queue ) > 1 and Mnh.queue[ 1 ] >= K  ):
        return answer;
    else:
        return -1;
    return answer            


def getsc( x, y ):
    return x + ( y * 2 );
#correct
def solution3(scoville, K):
    import heapq;
    heapq.heapify( scoville );
    answer = 0;
    lenx = len( scoville ) 
    while( lenx > 1 and scoville[0] < K ):
        val1,val2 = heapq.heappop( scoville ),heapq.heappop( scoville );
        sc = getsc( val1, val2 );
        heapq.heappush( scoville, sc );
        answer+=1;
        lenx -= 1;
    
    if( lenx >= 1 and scoville[ 0 ] >= K ):
        return answer;
    else:
        return -1;
        
        
    return answer

solution( [ 1 ,1,5,6 ], 7)