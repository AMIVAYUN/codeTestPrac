# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:12:21 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''
1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

'''

N = int( input() );

layers = [ ];

starts = list( map( int, input().split() ) );

for i in range( N - 1 ):
    lst = list( map( int, input().split() ) );   
    layers.append( lst );
    
answer = float( 'inf' );
Mn = float( 'inf' );
for start in range( 3 ):
    
    

    dp = [ [ 0 ] * 3 for _ in range( N - 1 ) ];
    
    
    
    
    for i in range( N - 1 ):
        
        for j in range( 3 ):
            
            if( ( i == N - 2 or i == 0 ) and j == start ):
                dp[ i ][ j ] = float( 'inf' );
                continue;
                
            bias1 , bias2 = ( j + 1 ) % 3 , ( j - 1 ) % 3;
    
                    
            dp[ i ][ j ] = min( dp[ i - 1 ][ bias1 ] , dp[ i - 1 ][ bias2 ] ) + layers[ i ][ j ];
        
    
    for i in range( 3 ):
        dp[ -1 ][ i ] += starts[ start ];
   
    print( start );
    for row in dp:
        print( row )

    Mn = min( Mn, min( dp[ N - 2 ] ) );
    



        

print( Mn );

'''

SOL1 WA
for i in range( N ):
    sum_ = layers[ 0 ][ i ];
    idxlst = [ 0 ] * N;
    idxlst[ 0 ] = i;
    for idx in range( 1, N ):
        
        if( sum_ >= answer ):
            continue;
        if( idx == N - 1 ):
            Mn = float( 'inf' );
            t = idx - 1;
            for k in range( N ):
                if( k == idxlst[ idx - 1 ] ):
                    continue;
                elif( k == idxlst[ 0 ] ):
                    continue;
                if( k == idxlst[ idx - 1 ] ):
                    continue;
                if( Mn >= layers[ idx ][ k ] ):
                    t = k;
                    Mn = layers[ idx ][ k ];
            
            sum_ += Mn;
            idxlst = t;
            print( idx, sum_, i, t, idxlst )
            continue;
            

        Mn = float( 'inf' );
        t = idx - 1;
        for k in range( N ):
            if( k == idxlst[ idx - 1 ] ):
                continue;
            if( Mn > layers[ idx ][ k ] ):
                t = k;
                Mn = layers[ idx ][ k ];
        
        idxlst[ idx ] = t;
        
        sum_ += Mn
        
        print( idx, sum_, i, t, idxlst )
        answer = min( sum_, answer );
    
        
        
'''      
    