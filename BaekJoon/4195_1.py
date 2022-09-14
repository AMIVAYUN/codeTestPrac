# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:19:57 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
    
    
    
    
1
4
a b
b c
c a
b a



1
7
a b
b c
c a
d e
e d
d e
a b

correct

2
3
3
2
2
2
3

    
"""
def check( a ):
    global dit, cnt;
    if( a not in dit ):
        dit[ a ] = cnt;
        cnt += 1;
    
    return dit[ a ];

def find( a ):
    global value,rank,cnt;
    
    if( value[ a ] != a ):
        value[ a ] = find( value[ a ] )
    return value[ a ];

def union( a, b ):
    global value;
    va, vb = find( a ), find( b );
    if( va == vb ):
        return;
    if( va < vb ):
        
        rank[ value[ va ] ] += rank[ value[ vb ] ];
        value[ vb ] = va
        
        
    else:
        rank[ value[ vb ] ] +=  rank[ value[ vb ] ];
        value[ va ] = vb
        
        
        
    
cnt = 0;

dit = {};

T = int( input() );


for i in range( T ):
    n = int( input() );
    
    value = [ i for i in range( n * 2 ) ]
    rank = [ 1 for _ in range( n * 2 ) ] 
    for i in range( n ):
        
        a, b = input().split()
        
        num1, num2 = check( a ), check( b );
        
        union( num1, num2 );
        
        print( rank[ find( num1 ) ] )
       
        