# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 14:06:35 2022
@FileName: 15686.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/15686
"""



N, M = map( int, input().split() );

graph = [];


chicken = [];
house = [];
rs = ( N**3 ) * M ;
for x in range( N ):
    ROW = list( map( int, input().split() ) );
    for y in range( N ):
        if( ROW[ y ] == 1 ):
            
            house.append( ( x, y ) );
        
        elif( ROW[ y ] == 2 ):
            
            chicken.append( ( x, y ) );
            


def getDist( pos1, pos2 ):

    return abs( pos1[ 0 ] - pos2[ 0 ] ) + abs( pos1[ 1 ] - pos2[ 1 ] );

def getChickDist( house, chicken ):

    global N;
    dists = [ N**2 ] * len( house );
    
    for chick in chicken:
        
        for j in range( len( house ) ):
            
            dists[ j ] = min( dists[ j ], getDist( house[ j ], chick ) );
    
    return sum( dists );

    
import itertools

for i in range( 1, M  + 1 ):
    cmb = list( itertools.combinations( chicken, i ) );
    for chick in cmb:
        sub =  getChickDist(house, chick);
        
        rs = min( rs, sub )

    
    

print( rs )