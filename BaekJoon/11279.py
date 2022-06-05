# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 19:34:24 2022
@FileName: 11279.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11279
"""

# 앞으로 입력은 sys.stdin.readline()으로 받자.

import sys;
def main():
    import heapq;
    n = int( sys.stdin.readline() );
    lst = [];
    heapq.heapify( lst );
    for i in range( n ):
        k = int( sys.stdin.readline() );
        if( k ):
            heapq.heappush( lst, ( -k , k ) )
        else:
            if( len( lst ) > 0 ):
                print( heapq.heappop( lst )[ 1 ] );
                
            else:
                print( 0 );

            


if( __name__ == "__main__"):
    main();