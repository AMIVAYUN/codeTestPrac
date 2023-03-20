# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:07:18 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


#1644

#https://www.acmicpc.net/problem/1644

# 완탐 TIMEOUT
def isPrime( n ):
    if( n == 2 or n == 3 ):
        return True;
    for i in range( 2, int( n ** 0.5 ) + 1 ):
        if( n % i == 0 ):
            return False;
    
    return True;
n = int( input() );
dp = [ 0 ] * ( n + 1 );
lst = [];
for i in range( 2, n + 1 ):
    if( isPrime( i ) ):
        lst.append( i )


for idx in range( len( lst ) ):
    for bias in range( len( lst ) ):
        if( idx + bias > len( lst ) or n < idx + bias ):
            continue;
        val = sum( lst[ idx: idx + bias ] );
        if( val > ( n ) ):
            continue;

        dp[ val ] += 1 ;

print( dp[ n ] );
    

#SOL2
# WA PREFIX SUM TIMEOUT
def isPrime( n ):
    if( n == 2 or n == 3 ):
        return True;
    for i in range( 2, int( n ** 0.5 ) + 1 ):
        if( n % i == 0 ):
            return False;
    
    return True;
n = int( input() );

lst = [];
for i in range( 2, n + 1 ):
    if( isPrime( i ) ):
        lst.append( i )
        
leng = len( lst )
prefix_sum = [ 0 ] * leng;
prefix_sum[ 0 ] = lst[ 0 ];
answer = 0;

for idx in range( 1, leng ):
    prefix_sum[ idx ] = prefix_sum[ idx - 1 ] + lst[ idx ];
    if( prefix_sum[ idx ] == n ):
        answer += 1;

for idx in range( 1, leng ):
    for bias in range( idx ):
        
        if prefix_sum[ idx  ] - prefix_sum[ bias ] == n:
            answer += 1;
print( answer )


#sol3 WA

def isPrime( n ):
    if( n == 2 or n == 3 ):
        return True;
    for i in range( 2, int( n ** 0.5 ) + 1 ):
        if( n % i == 0 ):
            return False;
    
    return True;

n = int( input() );

def calc( n ):
    
    lst = [];
    if( 1 < n < 4 ):
        return 1;
    
    elif( n <= 1 ):
        return 0;
    
    for i in range( 2, n + 1 ):
        if( isPrime( i ) ):
            lst.append( i )

    leng = len( lst );
   
    prefix_sum = [ 0 ] * leng;
    prefix_sum[ 0 ] = lst[ 0 ];
    answer = 0;
    
    
    
    for idx in range( 1, leng ):
        prefix_sum[ idx ] = prefix_sum[ idx - 1 ] + lst[ idx ];
        if( prefix_sum[ idx ] == n ):
            answer += 1;

    for idx in range( leng ):
        # N ^ 2 을 N LOG N 으로
        lt = idx; rt = leng - 1;

        while lt <= rt:
            mid = ( lt + rt ) // 2;

            if( prefix_sum[ mid ] - prefix_sum[ idx ] == n):
                answer += 1;
                break;

            if( prefix_sum[ mid ] - prefix_sum[ idx ] < n ):
                lt = mid + 1;

            else:
                rt = mid - 1;


    return answer;

print( calc( n ))