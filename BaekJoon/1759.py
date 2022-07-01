# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def chkAns( N, str0 ):
    chk = [ "a","e","i","o","u"]
    
    cnt = 0;
    
    for i in chk:
        if( i in str0 ):
            cnt += 1;
        
    return N - cnt > 1 and cnt > 0

L, C = map( int,  input().split() );

slst = input().split();


import itertools;

val = list ( itertools.combinations( sorted( slst ) , L) )


for i in val:
    str0 = "".join( j for j in i )
    if( chkAns( L, str0) ):
        print( str0 );

    