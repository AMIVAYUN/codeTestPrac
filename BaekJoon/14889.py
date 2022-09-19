# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:04:35 2022
@FileName: 14889.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/14889
"""
def getVal( a, b ):
    return graph[ a ][ b ] + graph[ b ][ a ];

def getTeamVal( team ):
    
    sum_ = 0;
    for case in itertools.combinations( team, 2 ):
        sum_ += getVal( case[ 0 ], case[ 1 ] );
        
        
    return sum_
N = int( input() );

Mn = 0;

graph = [];

for i in range( N ):
    graph.append( list( map( int, input().split() ) ) );
    
    Mn += sum( graph[ i ] )
    
lst = [ i for i in range( N ) ];

sett = set( lst )

import itertools;
'''
12 34// 13 24// 14 23  24 
'''
Stan = N // 2;

cmb = itertools.combinations( lst, Stan );


for case in list( cmb ):
    tmp = set( case );
    
    Mn = min( Mn, abs( getTeamVal( tmp ) - getTeamVal( sett - tmp ) ) )

             
print( Mn );


    
