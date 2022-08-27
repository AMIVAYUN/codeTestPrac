# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:36:27 2022
@FileName: 2792.py
@author: YUNJUSEOK
@Link: https://acmicpc.net/problem/2792
"""


N, M = map( int, input().split() );

colors = [];

sum_ = 0;

Mx = 0;
for i in range( M ):
    color = int( input() );
    sum_ += color;
    Mx = max( Mx, color );
    colors.append( color ) ;

lt = 0; rt = Mx;

ans = 0;

while lt<= rt:
    mid = ( lt + rt ) // 2 ;
    
    canbe = 0;
    if( mid == 0 ):
        lt = lt + 1;
        continue;
        
    for i in colors:
        n, r = divmod( i, mid );
        canbe += n;
        if( r ):
            canbe += 1;
    

    
    if( canbe > N ):
        lt = mid + 1;
        
    else:
        ans = mid;
        rt = mid - 1


print( ans )