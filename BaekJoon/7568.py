# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 13:49:13 2022
@FileName: 7568.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/7568
"""

'''
N = int( input() );
lst = []
for i in range( N ):
    a, b = map( int, input().split() );
    
    lst.append( ( a, b ,i ) );
    
lst = sorted( lst, key = lambda x: x[ 0 ] and x[ 1 ] , reverse = True );

rank = 1;

idx = 0;

rs = [ 0 ] * N;
start = 0;
len1 = 1;


while idx < N:
    
    while idx < N - 1 and not( lst[ idx ][ 0 ] > lst[ idx + 1 ][ 0 ] and lst[ idx ][ 1 ] > lst[ idx + 1 ][ 1 ] ):
        idx += 1;
        len1 += 1;
    for j in range( start, idx + 1 ):
        rs[ lst[ j ][ 2 ] ] = rank;
    
    start = idx + 1;
    idx += 1;
    rank += len1;
    len1 = 1;
'''
N = int( input() );
lst = []
for i in range( N ):
    a, b = map( int, input().split() );
    
    lst.append( ( a, b ) );
rs = [ 0 ] * N 
for i in range( N ):
    count = 1;
    for j in range( N ):
        if( lst[ i ][ 0 ] < lst[ j ][ 0 ] and lst[ i ][ 1 ] < lst[ j ][ 1 ] ):
            count+= 1;
    
    rs[ i ] = count;

for i in rs:
    print( i, end = " " );