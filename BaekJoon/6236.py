# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:38:49 2022
@FileName: 6236.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/6236
"""


N, M = map( int, input().split() );
lst = [];
sum_ = 0
Mx = 0;
for i in range( N ):
    tg = int( input() )
    lst.append( tg );
    sum_ += tg
    Mx = max( Mx, tg );
#0 이면 반례에 걸림
lt = Mx; rt = sum_*10;

ans = 0;

while lt <= rt:
    mid = ( lt + rt ) // 2;
    cnt = 1;
    money = mid;
    
    for i in range( N ):
        if( money < lst[ i ] ):
            money = mid;
            cnt += 1;
        
        money -= lst[ i ];

    if( cnt > M ):
        lt = mid + 1;
        
    else:
        ans = mid;
        rt = mid - 1;
    
    
print( ans )
