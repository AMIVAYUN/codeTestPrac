# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:19:43 2022
@FileName: 1351.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1351
"""
#Memory Out
def main1():
    N,P,Q = map( int, input().split() );
    
    lst = [ 1 ];
    
    for i in range( 1, N + 1 ):
        pi = i//P;
        pq = i//Q;
    
        lst.append( lst[ pi ] + lst[ pq ] );
        
    print( lst[ N ] );


# 68% Time Out
def main2():
    N,P,Q = map( int, input().split() );
    
    print( getNum( N,P,Q ) )
    
def getNum( N, P, Q ):
    
    if( N == 0 ):
        return 1;
    
    return( getNum( N//P, P, Q ) + getNum( N//Q, P, Q ) )

# Using Top - down and Memoization

dit = { 0: 1 };
def main():
    N,P,Q = map( int, input().split() );
    
    print( getNum( N,P,Q ) )
    
def getNum( N, P, Q ):
    global dit;
    if( N in dit ):
        return dit[ N ];
    pi = getNum( N//P, P, Q );
    pq = getNum( N//Q, P, Q )
    
    dit[ N//P ] = pi
    dit[ N//Q ] = pq
    return pi + pq
    





if( __name__ == "__main__" ):
    main();