# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 16:15:18 2022
@FileName: 12015 & 11053.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/12738
"""

def main():
    N = int( input() )
    A = [ int( i ) for  i in input().split() ];
    
    lst = [ 1 ] * N
    for i in range( N ):
        for j in range( i ):
            if( A[ i ] > A[ j ] ):
                lst[ i ] = max( lst[ j ] + 1, lst[ i ])
                
    
    print( max( lst ) )
    
'''
-- 12738
'''
def index( lst, num ):
    lt, rt = 0, len( lst ) - 1;
    answer = 0;
    while( lt <= rt ):
        mid = ( lt + rt ) // 2;
        if( lst[ mid ] >= num ):
            rt = mid - 1;
            answer =  mid;
            
        else:
            
            lt = mid + 1;
    
    return answer;
def main():
    N = int( input() )
    A = [ int( i ) for i in input().split() ];
    lst = [ A[ 0 ] ];
    for i in range( 1, N ):
        if( lst[ - 1 ] < A[ i ] ):
            lst.append( A[ i ] );
        else:
            idx = index( lst, A[ i ] );
            lst[ idx ] = A[ i ]
    
    print( len( lst ) )
    
if( __name__ == "__main__"):
    main()    
    
        
if( __name__ == "__main__"):
    main()