# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:15:43 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N, K = map( int, input().split() );




cnt = 0;


while bin( N ).count( '1' ) > K:

    idx = bin(N)[::-1].index('1');
    cnt += 2**idx;
    N += 2 ** idx;

print( cnt if bin( N ).count( '1' ) == K else -1 ) 


'''
dq.append( ( N, 0, 1 ) ) ;

while dq:
    
    now, cnt, depth = dq.popleft();
    
    if( now == K ):
        Mx = min( cnt, Mx );
        continue;
    
    if( now % 2 ):
        dq.append( (now + 1, cnt + depth, depth) );
    
    else:
        if( now // 2 >= K ):
            dq.append( (now // 2, cnt , depth * 2) );
            

'''


'''
while now != K:

    if( now % 2 ):
        now += 1;
        cnt += depth;
        
    
    else:
        now //= 2;
        depth *= 2;

print( cnt )


'''