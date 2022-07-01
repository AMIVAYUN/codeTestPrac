# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 19:07:00 2022
@FileName: 이상한 술집.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/13702
"""


N, K = map( int, input().split() );

pot = [];
Mx = 0;

if( K == 0 or N == 0 ):
    print( 0 );
else:
    for i in range( N ):
        inp = int( input() ) ;
        Mx = inp if Mx < inp else Mx;
        pot.append( inp );
        
        

    lt = 0 ;rt = Mx;
    ans = 0;
    while( lt<= rt ):
        mid = ( lt + rt ) // 2;
        temp = pot[:]
        cnt = 0;
        
        while temp:
            val = temp.pop();
            
            if( mid ):
                cnt += val // mid
                
            else:
                cnt += int( val > mid )
            
        if( cnt >= K ):
            ans = mid
            lt = mid + 1;
            
        else:
            rt = mid - 1;
        
        
            
        

    print( ans );

    

