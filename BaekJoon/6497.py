# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:43:20 2022
@FileName: 6497.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/6497
"""
'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
4 6 11
'''

# 50% Time out
'''



while True:
    m, n = map( int, input().split() );
    sum_ = 0;
    graph = [];
    lst = [];
    
    if( m == 0 and n == 0 ):
        break;
    for i in range( n ):
        x, y, cost = map( int, input().split() );
        
        lst.append( tuple( sorted( (x, y) )  ) + ( cost, ) )
        
        sum_ += cost;
    
        lst = list( sorted( lst , key = lambda x: x[ 2 ] ) );
        
    costs = [];        
        
    minimumNode = [ [ i ] for i in range( m ) ]
    for vertex in lst:
        n1, n2, cost = vertex[ 0 ], vertex[ 1 ], vertex[ 2 ];
        if( minimumNode[ n1 ] != minimumNode[ n2 ] ):
            tg = min( minimumNode[ n1 ], minimumNode[ n2 ] );
            cg = max( minimumNode[ n1 ], minimumNode[ n2 ] );
            for i in range( m ):
                if( minimumNode[ i ] == cg ):
                    minimumNode[ i ] = tg;
            costs.append( cost );
            
            
                
        
    print( sum_ - sum( costs ) );      


'''

# 50% Time Out;
'''
def parent( node ):
    global minimumNode;
    
    pos = node;
    while pos != minimumNode[ pos ]:
        pos = minimumNode[ pos ];
    
    return pos;
'''
# 50% TimeOut
'''
def parent( node ):
    global minimumNode;
    
    if( minimumNode[ node ] == node ):
        return node;
    else:
        return parent( minimumNode[ node ] )
'''
'''

def plus( a, b ):
    global minimumNode;
    if( a > b ):
        minimumNode[ a ] = b;
        
    else:
        minimumNode[ b ] = a

'''


def plus( a, b ):
    global minimumNode;
    
    a = parent( a );
    
    b = parent( b );
    
    if( a > b ):
        minimumNode[ a ] = b;
        
    else:
        minimumNode[ b ] = a


def parent( node ):
    global minimumNode;
    
    if( minimumNode[ node ] == node ):
        return node;
    
    else:
        node = parent( minimumNode[ node ] );
        return node;
    
while True:
    m, n = map( int, input().split() );
    sum_ = 0;
    lst = [];

    
    
    if( m == 0 and n == 0 ):
        break;
        
        
        
    for i in range( n ):
        x, y, cost = map( int, input().split() );
        
        lst.append( ( x, y, cost ) )
        
    
    lst = list( sorted( lst , key = lambda x: x[ 2 ] ) );
        
    costs = [];        

    minimumNode = [  i  for i in range( m ) ]
    for vertex in lst:
        n1, n2, cost = vertex[ 0 ], vertex[ 1 ], vertex[ 2 ];

        
        if( parent( n1 ) != parent( n2 ) ):
            plus( n1, n2 );
            
        
            continue;
        
        #costs.append( cost );
        sum_ += cost;
  
            
            
                
        
    print( sum_ );     
    
