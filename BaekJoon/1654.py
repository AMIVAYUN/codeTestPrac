# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 12:46:23 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''
N개의 랜선

자체적으로 K개의 랜선을 가지고 있음. ( 길이가 제각각 );

N개의 랜선을 같은 길이의 랜선으로 만들고 싶었다.

ex_ 300cm    140 * 2 + 20;

'''


K, N = map( int, input().split() );

Line = [];

for i in range( K ):
    Line.append( int( input() ) ) ;
    

Mx = max( Line );

ans = Mx;

lt = 0 ; rt = Mx;
while lt<= rt:
    mid = ( lt + rt ) // 2;
    
    if ( mid == 0 ):
        lt = mid + 1;
        continue
    sum_ = 0;
    for line in Line:
        
        sum_ += ( line ) // mid;
    
    
    if( sum_ >= N ):
        lt = mid + 1 ;
        
        ans = mid;
    else:
        
        rt = mid -1 ;
        
print( ans )
        