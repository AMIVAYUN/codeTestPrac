# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:21:18 2023

@author: 주석
"""
import sys;
sys.setrecursionlimit( int( 1e6 ) );

class Node:
    def __init__( self, idx ):
        self.val = idx;
        self.childs = [];
        self.parent = [];
    
    
    def getSum( self ):
        global dp;
        sum_ = self.time;
        Mx = 0;
        for child in self.childs:
            if( dp[ child.val ] != -1 ):
                Mx =max( Mx, dp[ child.val ] );
                continue;
            
            Mx = max( Mx, child.getSum() ); 
        
        dp[ self.val ] = sum_ + Mx;
        return sum_ + Mx;


T = int( input() );

for c in range( T ):
    N, K = map( int, input().split() );
    
    
    a = list( map( int, input().split() ) );
    
    
    nodelst = [ Node( i ) for i in range( N + 1 ) ];
     
    dp = [ -1 ] * ( N + 1 );
    
    #visit = [ 1 ] * ( N + 1 ); 
    
    for i in range( K ):
        x, y = map( int, input().split() );
        nodelst[ x ].parent.append( nodelst[ y ] );
        nodelst[ y ].childs.append( nodelst[ x ] );
    
    nodelst = nodelst[ 1 : ];
    
    
    for i in range( N ):
        nodelst[ i ].time = a[ i ];
        
    
    target = int( input() );
    
    
    print( nodelst[ target - 1 ].getSum() );
    

