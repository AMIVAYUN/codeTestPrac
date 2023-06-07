# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:39:35 2023

@author: 주석
"""
n, m = map( int, input().split() );

lst = list( map( int, input().split() ) );

plus = [];

minus = [];

for i in lst:
    if( i >= 0 ):
        plus.append( i );
    else:
        minus.append( i );
        
        
plus = list( sorted( plus , key = lambda x: -x ) );

minus = list( sorted( minus ) );

dists = [];

for i in range( len( plus ) ):
    # [ 100, 15, 10 1 ] , m == 2 >> 100, 10 
    if( i % m == 0 ):
        dists.append( plus[ i ] );

for i in range( len( minus ) ):
    if( i % m == 0 ):
        dists.append( abs( minus[ i ] ) );

dists = list( sorted( dists ) );



print( sum( dists[: -1 ] ) * 2 + dists[ -1 ] );

'''
7 2
-37 2 -6 -39 -29 11 -28
'''
'''

#sol2 WA
n, m = map( int, input().split() );

lst = list( map( int, input().split() ) );


lst = list( sorted( lst ) );

for idx in range( n ):
    if( lst[ idx ] >= 0 ):
        break;

from collections import deque;
plus = deque( lst[ idx: ] );

minus = deque( sorted( lst[ : idx ], key = lambda x: -x ) );


pos = 0;

cnt = 0;

while plus or minus:
    print( plus, minus )
    print( 'cnt: ', cnt );
    nextplus = [];
    nextminus = [];
    flag = True
    
    ifflag = False;
    
    if( not minus or ( plus and minus and abs( minus[ 0 ] ) > plus[ 0 ] ) ):
        ifflag = True;
    
    if( ifflag ):
        if( len( plus ) <= m ):
            while plus:
                nextplus.append( plus.popleft() );
        else:
        
            for i in range( m ):
                if( not plus ):
                    break
                if( nextplus and len( plus ) >= 2 and ( plus[ 0 ] - nextplus[ -1 ] ) > ( plus[ 1 ] - plus[ 0 ] ) ):
                    break;
            
                nextplus.append( plus.popleft() );
        
        
            
    else:
        flag = False;
        if( len( minus ) <= m ):
            while minus:
                nextminus.append( minus.popleft() );
        else:
            for i in range( m ):
                if( not minus ):
                    break;
                if( nextminus and len( minus ) >= 2 and abs( minus[ 0 ] - nextminus[ -1 ] ) > abs( minus[ 1 ] - minus[ 0 ] ) ):
                    break;
            
                nextminus.append( minus.popleft() );
    
        
    next = nextplus if flag else nextminus;
    
    if( not plus and not minus ):
        cnt += next[ -1 ] if flag else -next[ -1 ]; 
    else:
        cnt += next[ -1 ] * 2 if flag else next[ -1 ] * -2;
            

print( cnt )
'''
'''
import heapq; 

#sol1
문제 잘 읽기 번당 M권임 이건 한권이고

'''
'''
n, m = map( int, input().split() );

lst = list( map( int, input().split() ) );


minus = [];
plus = [];


heapq.heapify( plus );
heapq.heapify( minus );

for i in lst:
    if( i >= 0 ):
        heapq.heappush( plus, i );
    else:
        heapq.heappush( minus, -i );


print( plus, minus )


pos = 0;
cnt = 0;

while ( plus or minus ):
    print( plus, minus )
    print( "cnt: ", cnt )
    print( "pos: " , pos )
    nextplus = heapq.heappop( plus ) if plus else float( 'inf' );
    nextminus = heapq.heappop( minus ) if minus else float( 'inf' );
    nextpos = pos;

    if( pos > 0 ):
        goplus = nextplus - pos
        gominus = pos + nextminus
        
        if goplus > gominus:
            if goplus != float( 'inf' ):
                heapq.heappush( plus, nextplus );
            cnt += gominus;
            pos = -nextminus;
        
        else:
            if gominus != float( 'inf' ):
                heapq.heappush( minus, nextminus );
            cnt += goplus;
            pos = nextplus
            
            
    elif( pos < 0 ):
        goplus = nextplus - pos
        gominus = nextminus + pos

        if goplus > gominus:
            if goplus != float( 'inf' ):
                heapq.heappush( plus, nextplus );
            cnt += gominus;
            pos = -nextminus;
        
        else:
            if gominus != float( 'inf' ):
                heapq.heappush( minus, nextminus );
            cnt += goplus;
            pos = nextplus
            
    else:
        goplus = nextplus
        gominus = nextminus

        if goplus > gominus:
            if goplus != float( 'inf' ):
                heapq.heappush( plus, nextplus );
            cnt += gominus;
            pos = -nextminus;
        
        else:
            if gominus != float( 'inf' ):
                heapq.heappush( minus, nextminus );
            cnt += goplus;
            pos = nextplus
            

print( cnt );
'''