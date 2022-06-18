# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 21:18:28 2022
@FileName: 3077.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/3077
"""
#3077

N = int( input() );
dit = {};

str0 = input().split();

str1 = input().split();

for i in range( N ):
    dit[ str0[ i ] ] = i

sum0 = 0;

for i in range( N - 1 ):
    for j in range( i + 1, N ):
        sum0 += dit[ str1[ i ] ] < dit[ str1[ j ] ];
print( str( sum0 )+"/"+str( ( N**2 - N ) // 2))

#3077_1

N = int( input() );


str0 = input().split();
dit = { str0[ i ] : str0[ i + 1: ]  for i in range( N ) }
str1 = input().split();
dit1 = { str1[ i ] : str0[ i + 1: ]  for i in range( N ) }
sum0 = 0;

for i in dit1:
    for j in dit1[ i ]:
        sum0 += j in dit[ i ]
print( str( sum0 )+"/"+str( ( N**2 - N ) // 2))

#3077_2

N = int( input() );
dit = {};
dit1 = {};

str0 = input().split();

str1 = input().split();

for i in range( N ):
    dit[ str0[ i ] ] = str0[ i + 1 : ]
    dit1[ str1[ i ] ] = str1[ i + 1 : ]

sum0 = 0;

for i in dit1:
    for j in dit1[ i ]:
        sum0 += j in dit[ i ]
print( str( sum0 )+"/"+str( ( N**2 - N ) // 2))