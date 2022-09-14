# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:00:32 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""



def find( a ):
    global dit;
    
    if( dit[ a ] != a ):
        dit[ a ] = find( dit[ a ] )
    return dit[ a ];

def union( a, b ):
    global rank;
    
    if( a!= b and( find( a ) != find( b ) )):
        
        
        val = find( a )
        rank[ val ] += rank[ find( b ) ];
        dit[ b ] = val;
        

        
        
        


T = int( input() );


for i in range( T ):
    n = int( input() );
    dit = {};
    rank = {}
    for i in range( n ):
        
        a, b = input().split()
        
        if( a not in dit ):
            dit[ a ] = a;
            rank[ a ] = 1;
        if( b not in dit ):
            dit[ b ] = b;
            rank[ b ] = 1;
        
        union( a, b );
        
        print( rank[ find( a ) ] )
       
        