# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:48:25 2022
@FileName: 2075.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2075
"""


import heapq;
#7% Memory Out
def t1():
    import heapq;


    N = int( input( ) );
    
    
    target = N **2 - N;
    
    heap = []
    heapq.heapify( heap )
    
    for i in range( N ):
        nums = list( map( int, input().split() ) );
        
        for num in nums:
            heapq.heappush(heap, num);
            
            
            
    
    for i in range( target ):
        heapq.heappop( heap );
        
    
    print( heap[ 0 ] )
    
#WA
def t2():
    
    N = int( input( ) );
    
    
    target = N **2 - N;
    graph = [];
    heap = []
    heapq.heapify( heap )
    cnt = 0;
    Mx = 0;
    for i in range( N ):
        nums = list( map( int, input().split() ) );
        
        Mx = max( Mx, max( nums ) );
        
        heapq.heappush( heap, Mx );
        
    print( heap[ 0 ] )


#7% Memory Out 
def t3():
    import bisect;
    
    lst = [];
    
    
    N = int( input() );
    
    for i in range( N ):
        nums = list( map( int, input().split() ) );
        
        for num in nums:
            bisect.insort( lst, num );
            
    
    print( lst[ -1 * N ] )
   
def t4():
    import bisect;
    
    
    
    N = int( input() );
    lst = [ -10 ** 8 ] * N;
    
    for i in range( N ):
        nums = list( map( int, input().split() ) );
        
        for num in nums:
            bisect.insort( lst, num );
            lst.pop( 0 )
    
    print( lst[ 0 ] )

t4()    


        

