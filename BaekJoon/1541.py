# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 15:45:35 2022
@FileName: 1541.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1541
"""

def add( a, b ):
    return a + b;
def sub( a, b ):
    return a - b;

plus = 0; minus = 1;
str0 = input();
str1 = ""
oper = ["+","-"]
oper1 = [];
dit = { "+": add, "-": sub }

lst = [];
for i in str0:
    if i in oper:
        lst.append( int( str1 ) )
        str1 = ""
        oper1.append( i )
    else:
        str1 += i;

lst.append( int( str1 ) )
start = lst[ 0 ]; lst = lst[ 1: ]
for i in range( len( oper1 ) ):
    if( i < len( oper1 ) and oper1[ i ] == oper[ minus ] ):
        idx = i + 1;
        while idx < len( oper1 ) and oper1[ idx ] != oper[ minus ]:
            oper1.pop( idx );
            lst[ i ] += lst.pop( idx );
            
            
for i in range( len( oper1 ) ):
    start = dit[ oper1.pop( 0 ) ]( start, lst.pop( 0 ) )

print( start )