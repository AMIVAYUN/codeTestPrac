# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:52:56 2023
@FileName: 1806.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1806
"""


N, obj = map( int, input().split() );

lst = list( map( int, input().split() ) );

prefix_sum = dict();

prefix_sum[ -1 ] = 0;

answer = N ;

for idx in range( N ):
    prefix_sum[ idx ] = prefix_sum[ idx - 1 ] + lst[ idx ];

if( prefix_sum[ N - 1 ] < obj ):
    print( 0 );

else:
    
    for idx in range( N ):
        
        lt = idx;
        
        rt = N - 1;
        
        while lt <= rt:
            
            mid = ( lt + rt  ) // 2;
            
            if( prefix_sum[ mid ] - prefix_sum[ idx - 1 ] >= obj ):
                print( idx, mid )
                answer = min( answer , mid - idx + 1  );
                
       
                
                rt = mid - 1;
            
            else:
                lt = mid + 1;
            
                
    print( answer );
            