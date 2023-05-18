# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:59:56 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


# -*- coding: utf-8 -*-
'''
#S1 Memory Out
'''
dx = [ 0 , -1 , 0 , 1 ];

dy = [ 1, 0,  -1 , 0 ];


#graph = [ [ 0 ] * 10001 for _ in range( 10001 ) ];



start = ( 5000, 5000 );

idx = 1;
dist = 1;
#graph[ start[ 0 ] ][ start[ 1 ] ] = 1;
direc = 0;
cnt = 0;

from collections import deque;

dq = deque();


dq.append( ( start, cnt, idx, 2, direc ) );
'''
while dq:
    now, cnt, remain, val, direc = dq.popleft();
    if cnt == 2:
        cnt = 0;
        remain += 1;


    x, y = now;

    checker = 0;



    for i in range( remain ):
        x += dx[ direc ];
        y += dy[ direc ];

        if( 0 <= x < 10001 and 0 <= y < 10001 ):
            graph[ x ][ y ] = val;
            val += 1;
        else:
            checker = 1;


    if( checker ):
        continue;

    else:

        dq.append( ( ( x, y ), cnt + 1, remain, val, ( direc + 1 ) % 4 ) );
'''
r1, c1, r2, c2 = map( int, input().split() );

r1 += 5000;

c1 += 5000;

r2 += 5000;

c2 += 5000;

Mxlst = [ 0 ] * ( c2 - c1 + 1 );

s2graph = [ [ 0 ] * ( c2 + 1 - c1 ) for _ in range( r2 - r1 + 1 ) ];

from collections import defaultdict;

mapper = defaultdict( int );
Minx , Miny = 10001, 10001;

for i in range( r1, r2 + 1 ):
    for j in range( c1, c2 + 1 ):
        Minx = min( Minx, i - 5000 );
        Miny = min( Miny, j - 5000 );
        mapper[ ( i, j ) ] = ( i - 5000, j - 5000 );


for key in mapper.keys():

    mapper[ key ] = ( mapper[ key ][ 0 ] - Minx, mapper[ key ][ 1 ] - Miny );

if( start in mapper ):
    s2graph[ mapper[ start ][ 0 ] ][ mapper[ start ][ 1 ] ] = 1;

#s2
while dq:
    now, cnt, remain, val, direc = dq.popleft();
    if cnt == 2:
        cnt = 0;
        remain += 1;


    x, y = now;

    checker = 0;



    for i in range( remain ):
        x += dx[ direc ];
        y += dy[ direc ];

        if( 0 <= x < 10001 and 0 <= y < 10001 ):
            if( r1 <= x < r2 + 1 and c1 <= y < c2 + 1 ):
                newx, newy = mapper[ ( x, y ) ];
                s2graph[ newx ][ newy ] = val;
            #graph[x][y] = val;
            val += 1;
        else:
            checker = 1;


    if( checker ):
        continue;

    else:

        dq.append( ( ( x, y ), cnt + 1, remain, val, ( direc + 1 ) % 4 ) );





for i in range( r1, r2 + 1 ):
    idx = 0;
    for j in range( c1, c2 + 1 ):
        pos = mapper[ ( i, j ) ];
        Mxlst[ idx ] = max( Mxlst[ idx ], s2graph[ pos[ 0 ] ][ pos[ 1 ] ] );
        idx += 1;
result = [];
def getLength( num ):
    cnt = 0;
    while num > 0:
        num //= 10;
        cnt += 1;
    return cnt;
Mxlst = [ getLength( i ) for i in Mxlst ];

Mx = max( Mxlst );
for i in range( r2 - r1 + 1 ):
    for j in range( c2 - c1 + 1 ):
        print( str( s2graph [ i ][ j ] ).rjust( Mx ), end=" ")
    print()
'''
for i in range( r1, r2 + 1 ):
    str0 = "";
    idx = 0;
    for j in range( c1, c2 + 1 ):
        pos = mapper[(i, j)];
        target = str( s2graph[ pos[ 0 ] ][ pos[ 1 ] ] );
        str0 += (" " * (Mxlst[idx] - len(target) ) ) + target + " ";
        idx += 1;

    result.append( str0 );

for row in result:

    print( row );
'''
'''
#s1

for i in range( r1, r2 + 1 ):
    idx = 0;
    for j in range( c1, c2 + 1 ):

        Mxlst[ idx ] = max( Mxlst[ idx ], graph[ i ][ j ] );
        idx += 1;
result = [];
def getLength( num ):
    cnt = 0;
    while num > 0:
        num //= 10;
        cnt += 1;
    return cnt;
Mxlst = [ getLength( i ) for i in Mxlst ];



for i in range( r1, r2 + 1 ):
    str0 = "";
    idx = 0;
    for j in range( c1, c2 + 1 ):
        target = str( graph[ i ][ j ] );
        if( j == c1 ):
            str0 += (" " * (Mxlst[idx] - len(target))) + target;
        else:
            str0 += (" " * (Mxlst[idx] - len(target) + 1 ) ) + target;
        idx += 1;

    result.append( str0 );

for row in result:

    print( row );

'''