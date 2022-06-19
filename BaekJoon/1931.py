# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 14:02:34 2022
@FileName: 1931.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1931
"""

#1931 _ 1 82 %

N = int( input() );
lst = []

for i in range( N ):
    a, b = map( int, input().split() );
    lst.append( ( a, b ,b - a ) );

lst = sorted( lst, key = lambda x: ( x[ 0 ], x[ 2 ] ) )

proc = [ lst[ 0 ] ];

for i in range( 1, N ):
    if( proc[ -1 ][ 1 ] <= lst[ i ][ 0 ] ):
        proc.append( lst[ i ] );
    else:
        if( proc[ - 1 ][ 0 ]<= lst[ i ][ 0 ]< proc[ -1 ][ 1 ]and lst[ i ][ 1 ]<= proc[ -1 ][ 1 ] and lst[ i ][ 0 ] < proc[ -1 ][ 2 ] ):
            proc.pop();
            proc.append( lst[ i ] )

print( proc )

#1931 _ 2 87%


# 2 0 1 1 1

N = int( input() );
lst = []
dit = {};

end, timer = 0, 1
if( N == 0 ):
    print( 0 );
else:
    for i in range( N ):
        a, b = map( int, input().split() );
        #lst.append( ( a, b ,b - a ) );
        time = b - a;
        if( a not in dit ):
            dit[ a ] = ( b, time );
        elif( a in dit and time < dit[ a ][ 1 ] ):
            dit[ a ] = ( b, time );
    dit = sorted( dit.items(), key= lambda x: x[ 0 ] )
    proc = [ dit[ 0 ] ];    
    for i in range( 1, len( dit ) ):
        if(  proc[ -1 ][ 0 ]<= dit[ i ][ 0 ] <= proc[ -1 ][ 1 ][ end ] and dit[ i ][ 1 ][ end ] < proc[ -1 ][ 1 ][ end ] and dit[ i ][ 1 ][ timer ] <= proc[ -1 ][ 1 ][ timer ] ):

            proc.pop();
            proc.append(  dit[ i ] )

        else:
            if( proc[ -1 ][ 1 ][ end ]<= dit[ i ][ 0 ] ):
                proc.append( dit[ i ])

    print( len( proc ) )

    
    
    
    





#1931 _ 3 5%


# 2 0 1 1 1

N = int( input() );
lst = []
dit = {};

end, timer = 0, 1
if( N == 0 ):
    print( 0 );
else:
    for i in range( N ):
        a, b = map( int, input().split() );
        #lst.append( ( a, b ,b - a ) );
        time = b - a;
        if( a not in dit ):
            dit[ a ] = ( b, time ,1);
        elif( a in dit and time < dit[ a ][ 1 ] ):
            dit[ a ] = ( b, time ,1);
        
        elif( a in dit and time == dit[ a ][ 1 ]):
            dit[ a ] = ( b, time, dit[ a ][ 2 ] + 1 )
    dit = sorted( dit.items(), key= lambda x: x[ 0 ] )
    proc = [ dit[ 0 ] ];    
    for i in range( 1, len( dit ) ):
        if(  proc[ -1 ][ 0 ]<= dit[ i ][ 0 ] <= proc[ -1 ][ 1 ][ end ] and dit[ i ][ 1 ][ end ] < proc[ -1 ][ 1 ][ end ] and dit[ i ][ 1 ][ timer ] <= proc[ -1 ][ 1 ][ timer ] ):

            proc.pop();
            proc.append(  dit[ i ] )

        else:
            if( proc[ -1 ][ 1 ][ end ]<= dit[ i ][ 0 ] ):
                proc.append( dit[ i ])

    print( sum( i[ 2 ] for i in proc ) )

    
    
    
    





#1931 _ 4 35%
'''
# Case 1
10
4 7
2 2
1 9
2 9
3 7
4 7
2 7
4 7
1 5
2 2
'''

N = int( input() );
lst = [];

start, end = 0 , 1;

for i in range( N ):
    a, b = map( int, input().split() );
    lst.append( ( a, b ) );
        
lst = sorted( lst, key = lambda x: ( x[ start ], x[ end ] ) );
    
stack = [ lst[ 0 ] ] ;
for i in range( 1, N ):
    print( stack )
    if( stack[ -1 ][ start ] == lst[ i ][ start ] ):
        ## 여기가 문제 거꾸로 써버림if( stack[ -1 ][ end ] <= lst[ i ][ end ] ):
            stack.append( lst[ i ] )
            continue
    if( stack[ - 1 ][ end ] == lst[ i ][ start ] ):
        if( lst[ i ][ end ] >= stack[ -1 ][ end ] ):
            stack.append( lst[ i ] )
            continue;
        
    if( stack[ -1 ][ end ] < lst[ i ][ start ] ):
        stack.append( lst[ i ] );
        continue;
        
    elif( stack[ -1 ][ start ] < lst[ i ][ start ] < stack[ -1 ][ end ] ):
            
        if( lst[ i ][ end ] < stack[ -1 ][ end ] ):
            stack.pop();
            stack.append( lst[ i ] )
            continue;
    
print( len( stack ) )
        
    
    
    #1931 _ 5 35%
'''
# Case 1
10
4 7
2 2
1 9
2 9
3 7
4 7
2 7
4 7
1 5
2 2
'''

N = int( input() );
lst = [];

start, end = 0 , 1;

for i in range( N ):
    a, b = map( int, input().split() );
    lst.append( ( a, b ) );
        
lst = sorted( lst, key = lambda x: ( x[ start ], x[ end ] ) );
    
stack = [ lst[ 0 ] ] ;
for i in range( 1, N ):
    print( stack )
    if( stack[ -1 ][ start ] == lst[ i ][ start ] ):
        if( lst[ i ][ end ] <= stack[ -1 ][ end ] ):
            stack.append( lst[ i ] )
            continue
    if( stack[ - 1 ][ end ] == lst[ i ][ start ] ):
        if( lst[ i ][ end ] >= stack[ -1 ][ end ] ):
            stack.append( lst[ i ] )
            continue;
        
    if( stack[ -1 ][ end ] < lst[ i ][ start ] ):
        stack.append( lst[ i ] );
        continue;
        
    elif( stack[ -1 ][ start ] < lst[ i ][ start ] < stack[ -1 ][ end ] ):
            
        if( lst[ i ][ end ] < stack[ -1 ][ end ] ):
            stack.pop();
            stack.append( lst[ i ] )
            continue;
    
print( len( stack ) )
        
    
    #1931 _ 6 ans
'''
# Case 1
10
4 7
2 2
1 9
2 9
3 7
4 7
2 7
4 7
1 5
2 2
'''

N = int( input() );
lst = [];

start, end = 0 , 1;

for i in range( N ):
    a, b = map( int, input().split() );
    lst.append( ( a, b ) );
        
lst = sorted( lst, key = lambda x: ( x[ end ], x[ start ] ) );
    
stack = [ lst[ 0 ] ] ;
for i in range( 1, N ):
    print( stack )
    if( stack[ -1 ][ start ] == lst[ i ][ start ] ):
        if( lst[ i ][ end ] <= stack[ -1 ][ end ] ):
            stack.append( lst[ i ] )
            continue
    if( stack[ - 1 ][ end ] == lst[ i ][ start ] ):
        if( lst[ i ][ end ] >= stack[ -1 ][ end ] ):
            stack.append( lst[ i ] )
            continue;
        
    if( stack[ -1 ][ end ] < lst[ i ][ start ] ):
        stack.append( lst[ i ] );
        continue;
        
    elif( stack[ -1 ][ start ] < lst[ i ][ start ] < stack[ -1 ][ end ] ):
            
        if( lst[ i ][ end ] < stack[ -1 ][ end ] ):
            stack.pop();
            stack.append( lst[ i ] )
            continue;
    
print( len( stack ) )
        
    


