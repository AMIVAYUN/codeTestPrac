# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:52:18 2023

@author: 주석

빌딩 N개 선분

i번째 빌딩 i, 높이

"""


N = int( input() );


lst = list( map( int, input().split() ) );

'''
#SOL1 WA
def getCnt( lst, idx, leng ):
    
    cnt = 0;
    
    while idx < leng - 1 and lst[ idx + 1 ] >= lst[ idx ]:
        if lst[ idx + 1 ] == lst[ idx ]:
            idx += 1;
        else:
            cnt += 1;
            idx += 1;
    
    return cnt;


Mx = 0;

idx = 0;
cnt = 0;
while idx < N - 1:
    if( Mx != 0 and Mx > ( N - idx ) + cnt ):
        break;
    if( lst[ idx ] < lst[ idx + 1 ] ):
        cnt += 1;
        idx += 1;
    
    else:   
        print( idx, cnt );
        Mx = max( Mx, cnt + getCnt( lst, idx, N ) );
        idx += 1;
        cnt =1;


print( Mx );

'''
def getInc( pos1 , pos2 ):
    
    return ( pos2[ 1 ] - pos1[ 1 ] ) / ( pos2[ 0 ] - pos1[ 0 ] ) 

def getCnt( lst ):
    
    stan = ( 0, lst[ 0 ] );

    cnt = 0;
    leng = len( lst );
    if( leng == 1 ):
        return 0;
    
    
    if( leng < 2 ):
        return 1;
    
    now = -float( 'inf' );
    
    for i in range( 1, leng ):
        

        a = getInc( stan, ( i, lst[ i ] ) );
        if( now < a ):
            now = a;
            cnt += 1;
            
    return cnt;

Mx = 0;

for i in range( N ):
    cnt = 0;
    if( i == 0 ):
    
        cnt = getCnt( lst );
    elif( i == N - 1 ):
        cnt = getCnt( lst[ :: -1] );
        
    else:
        cnt += getCnt( lst[ i: ] );
        sub = lst[ : i + 1 ];
        
        cnt += getCnt( sub[::-1] );

    Mx = max( cnt, Mx );
     
print( Mx )
    
    


