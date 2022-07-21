# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:40:31 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
Mx = 1000000001

n, k = map( int, input().split() );

lst = [];

for i in range( n ):
    lst.append( int(input() ) );
lt = min( lst ); rt = Mx;
ans = 0;
while lt<= rt:
    mid = ( lt + rt ) // 2
    sum_ = 0;
    for i in range( n ):
        sum_ += mid - lst[ i ] if mid >= lst [ i ] else 0;
    
    if( sum_ <= k ):
        
        ans = mid;
        lt = mid + 1;
    else:
        rt = mid - 1;

print( ans )