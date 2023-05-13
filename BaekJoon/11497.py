# -*- coding: utf-8 -*-
"""
Created on Sat May 13 23:19:49 2023

@author: 주석
"""

T = int( input() );



from collections import deque;


for t in range( T ):
    N = int( input() );

    lst = list( map(int, input().split() ) );


    lst = deque( sorted( lst ) );
    
    turn = 0;
    dq = deque();
    Mx = 0;
    
    while lst:
        val = lst.popleft();
        
        if( turn % 2 ):
            dq.appendleft( val );
            if( turn > 1 ):
                Mx = max( Mx, abs( dq[ 0 ] - dq[ 1 ] ) );
        else:
            
            dq.append( val );
            if( turn > 1 ):
                Mx = max( Mx, abs( dq[ -1 ] - dq[ -2 ] ) )
            
        turn += 1;
        
    
    print( Mx );
        
    
    
    