# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:23:52 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N = int( input() );

lst = list( map( int, input().split() ) );

idx = int( input() );




from collections import defaultdict;
leaves = defaultdict( int );
graph = defaultdict( list );
root = N;


for i in range( N ):
    if( lst[ i ] == -1 ):
        root = i;
        continue
    
    if( i == idx ):
        continue;
        
    graph[ lst[ i ] ].append( i );
    


def postOrder( prev, now, graph ):
    global leaves;
    
    if( len( graph[ now ] ) == 0 ):
        return 1;
    
    sum_ = 0;
    flag = True;
    for child in graph[ now ]:
        sum_ += postOrder( now,child, graph );
        
    
    leaves[ now ] = sum_
    
    return sum_;
    
    
print( postOrder( None, root, graph ) if root != idx else 0);
'''
if( len( graph[ root ]) == 0 and root != idx ):
    
        print( 1 );

else:
    print( leaves[ root ] ) if root != idx else 0;
'''