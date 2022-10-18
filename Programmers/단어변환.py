# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:23:22 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(begin, target, words):
    from collections import defaultdict;
    import itertools;
    from collections import deque;
    
    lst = [ chr( ord( 'a') + i) for i in range( 26 )  ]
    

    vocab = defaultdict( int );
    
    Mn = 11;
    
    for word in words:
        vocab[ word ] += 1;
        
    dq = deque();
    
    checksum = 26 ** len( target )
    
    checker = defaultdict( int );
    
    dq.append(( begin, 0))
    
    while dq:
        print( dq, checker  )
        wd, cnt = dq.popleft()
        
        
        if( cnt > Mn ):
            continue;
        
        if( wd == target ):
            Mn = min( Mn, cnt );
            continue;
        if( sum( checker.values() ) == checksum ):
            break; 
        for idx in range( len( target ) ):
            if( wd[ idx ] == target[ idx ] ):
                continue;
            
            for ch in lst:
                
                tmp = wd[ :idx ] + ch + wd[ idx + 1: ]
            
                if( vocab[ tmp ] and checker[ tmp ] != 1 ):
                    checker[ tmp ] = 1;
                    dq.append( ( tmp, cnt + 1 ) );
            
        
    
    
    return Mn if Mn != 11 else 0;


#solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"] )

solution( "hit",	"cog",	["hot", "dot", "dog", "lot", "log"]	);