# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:54:49 2022
@FileName: 11723.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11723
"""
Mx = [ 1 << i for i in range( 1, 21 ) ]
Mx = sum( Mx )


setb = 0;
M = int( input() );

def getitem( num ):
    return 1 << num;


def add( num ):
    global setb;
    
    setb = setb | getitem( num );
    
def remove( num ):
    global setb;
    setb = setb & ~( getitem( num ) );

def check( num ):
    global setb;
    print( int( ( setb & getitem( num ) ) > 0 )  );

def all():
    global setb, Mx;
    setb = Mx;

def empty():
    global setb;
    setb = 0;
    
def toggle( num ):
    global setb;
    setb = setb ^ getitem( num );
    
import sys;

lst2 = [ 'all', 'empty' ];

for i in range( M ):
    str0 = sys.stdin.readline().split();
    if( str0 [ 0 ] not in lst2 ):
        if( str0[ 0 ] == 'add' ):
            add( int( str0[ 1 ] ) );
        elif( str0[ 0 ] == 'remove' ):
            remove( int( str0[ 1 ] ) );
        elif( str0[ 0 ] == 'check' ):
            check( int( str0[ 1 ] ) );
        elif( str0[ 0 ] == 'toggle' ):
            toggle( int( str0[ 1 ] ) )
        
    else:
        if( str0[ 0 ] == 'all' ):
            all();
        else:
            empty();
    
