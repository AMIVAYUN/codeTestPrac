# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:33:56 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
    
    00 01 02 03 04: 1 3 6 7 9
    
    11 12 13 14 2 5 6 8
    
    22 23 24 3 4 6
    
    33 34 1 3
    
    44 2
    
    
    v
    
    01 02 04
    
    13
    
    22 24
    
    34
    
    
"""



#SOL 2

answer = 0;

N, M = map( int, input().split() );

lst = list( map( int, input().split() ) );

prefix_sum = dict();

prefix_sum_res = [ 0 ] * M ;

prefix_sum[ -1 ] = 0;





for i in range( N ):
    
    prefix_sum[ i ] = prefix_sum [ i - 1 ] + lst[ i ];
    
    prefix_sum_res[ prefix_sum[ i ] % M ] += 1;
    
    if( prefix_sum[ i ] % M == 0 ):
        answer += 1
    
# 중복조합 공식으로 했으나 생각해보니 순열이었음.
for i in range( M ):
    if( prefix_sum_res[ i ] > 1 ):
        m = prefix_sum_res[ i ];
        answer +=  ( m * ( m - 1 ) ) // 2
  

print( answer )

#SOL 1 N^2
'''
answer = 0;

N, M = map( int, input().split() );

lst = list( map( int, input().split() ) );

prefix_sum = dict();

prefix_sum[ -1 ] = 0;

for i in range( N ):
    
    prefix_sum[ i ] = prefix_sum [ i - 1 ] + lst[ i ];
    


for bias in range( N - 1, -1 , -1 ):
    
    for i in range( -1, bias ):
        
        if( ( prefix_sum[ bias ] - prefix_sum[ i ] ) % M == 0 ):
            answer += 1;
            

print( answer )


'''