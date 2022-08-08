# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:56:09 2022
@FileName: 3079.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/3079

친구 M명 

공항에서 한줄로 N 개의 입국 심사대.

k번 심사대 -> ki 시간 걸림

한 심사대 -> 한번에 한사람

걸리는 모든 시간이 최소
    


"""

N, M = map( int, input().split() );
ans = 0;
K = [ 0 ] * N 

for i in range( N ):
    K[ i ] = int( input() );
    
print( K )
lt, rt = 0, max( K ) * M  + 1;

while( lt <= rt ):
    mid = ( lt + rt ) // 2;
    nPass = 0;
    
    for k in K:
        nPass += mid // k;
        if nPass >= M:
            break
    if nPass >= M:
        ans = mid;
        rt = mid - 1;
    else:
        lt = mid + 1 ;

print( ans )
    
    
