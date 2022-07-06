# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:06:28 2022
@FileName: 4673.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/4673
"""


'''
 
 i = n + getPos( n );

'''



def getPos( num ):
    str0 = str( num );
    sum0 = num;
    for i in range( len( str0 ) ):
        sum0 += int( str0[ i ] );
    
    return sum0;
def getPos2( num ):
    
    sum0 = num + sum( map( int, str( num ) ) );
    return sum0;
# 반례 11
def BS( target ):
    lt = 0; rt = target;
    ans = 0;
    while lt<= rt:
        print( lt, rt )
        mid = ( lt + rt ) // 2;
        num_ = getPos( mid );
        
        if( num_ > target ):
            rt = mid - 1;
        
        else:
            
            ans = mid;
            lt = mid + 1;
    
    print( ans , mid, getPos( ans ) )
    return getPos( ans ) == target;
            


def isSelf( num ):
    for i in range( num ):

        if( getPos( i ) == num ):
            return False;
    
    return True;

#Time out
def f1():
    
    
    for i in range( 1, 10001 ):
        if( isSelf( i ) ):
            print( i )
        

#by dp
'''
def f2():
    rs = [ 0 ] * 10001 ;
    
    for i in range( 10001 ):
        num_ = getPos( i )
        if( num_ < 10001 ):
            rs[ num_ ] = i;
    
    for j in range( 1, 10001 ):
        if( not( rs[ j ] ) ):
            print( j )
f2()
'''

def f2_1():
    rs= [ 0 ] * 10001;
    for i in range( 1, 10001 ):
        num_ = getPos2( i );
        if( num_ < 10001 ):
            rs[ num_ ] = i;
    
    for j in range( 1, 100 ):
        if( not( rs[ j ] ) ):
            print( j )
f2_1()