# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:05:31 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
import heapq;

lst = [];

heapq.heapify( lst );

n = int( input() );

for i in range( n ):
    heapq.heappush(lst, int( input() ) );
    
sum_ = 0;

while n > 1:
    a, b =heapq.heappop( lst ), heapq.heappop( lst );
    sum_ +=  a + b;
    heapq.heappush( lst, a + b );

    n -= 1;



print(  sum_ )