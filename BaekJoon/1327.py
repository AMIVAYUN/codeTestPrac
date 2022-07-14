# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:25:32 2022
@FileName: 1327.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1327
"""

import itertools;

n, k = map( int, input().split() );

lst = list( map( int, input().split() ) );

sub = sorted( lst );

from collections import deque;

perm = itertools.permutations( lst, n );

dq = deque();

dq.append( ( 0 ,lst [:] ) )


ans = [];

visit = { i : 1 for i in perm }

while dq:
    cnt, tmp = dq.popleft();
    
    if( tmp == sub ):
        ans.append( cnt );
        continue;
    
    for i in range( n - k + 1 ):
        tmp2 =  tmp[ :i ] + tmp[ i: i + k][ ::-1 ] + tmp[ i + k : ]
        if( visit[ tuple( tmp2 )] ):
            visit[ tuple( tmp2 ) ] = 0;
            
            
            dq.append( ( cnt + 1 , tmp2 ) ) 

print( min( ans ) if len( ans ) else -1  )
    
    
    
