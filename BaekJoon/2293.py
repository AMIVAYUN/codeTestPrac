# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:15:05 2022
@FileName: 동전1.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2293
"""
import sys;

sys.setrecursionlimit( int( 1e6 ) )



def t1():
    n, k = map( int, input().split() );

    coin = [];
     #try1 memory error
    rs = [];
    for i in range( n ):
        coin.append( int( input() ) ) ;
        
        
    def dfs( members ):
        global rs;
        if( sum( members ) ==  k ):
            rs.append( members );
            return
        
        for i in range( len( coin ) ):
            temp = members[:];
            temp.append( coin[ i ] );
            dfs( temp )
            
     
        
     
        

#dfs( [] );



def t2():
    n, k = map( int, input().split() );

    coin = [ 0 ] * 1000001;
     #try1 memory error
    
    
    for i in range( n ):
        coin[ int( input() ) ] += 1;

    for i in range( 1, k + 1 ):

        temp = [ 0 ];
        for j in range( 1, i ):
            temp.append( ( coin[ j ] + coin[ i - j ]  ) )
        
        temp.append( coin[ i ] );
        coin[ i ] = max( temp );
        
        
    print( coin[ k ] )
#t2();


def t3():
    n, k = map( int, input().split() );
    
    lst = [ 0 ] * 100001; # 0 오타


    coin = [];
     #try1 memory error
    
    
    for i in range( n ):
        coin.append( int( input() ) );
    
    for i in coin:
        lst[ i ] += 1;
        for j in range( i , k + 1 ):
            lst[ j ] = lst[ j ] + lst[ j - i ];
        
        
    print( lst[ :k + 1 ] )
    
t3()
def t4():
    
    n, k = map(int, input().split() );
    
    coins = []
    
    for _ in range(n):
        coins.append(int(input()))
    
    count_list = [0] * (k + 1)
    # x원짜리 동전 하나로 x원을 만드는 경우의 수 = 1
    count_list[0] = 1
    
    for i in coins:
        for j in range(i, k + 1):
            count_list[j] += count_list[j - i]
    
    print(count_list[ :k + 1 ])
    
t4()